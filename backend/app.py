import os
import io
import json
import time
import re
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai
from google.genai import types
from data import (
    ONET_QUESTIONS,
    SHS_PATHWAYS,
    INSTITUTIONS,
    ONET_ATTRIBUTION,
)


load_dotenv()
app = Flask(__name__)

# Allow all origins to ensure detailed error bodies pass through CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

SYSTEM_CONTEXT = """
You are assisting a Philippine Senior High School (SHS) guidance tool.
As of DepEd Memorandum No. 012, s. 2026 (Strengthened SHS Curriculum),
there are only 2 tracks: Academic and Technical Professional (TechPro).
Rigid strands no longer exist. Under Academic, a student can pick elective clusters: STEM, ABM, HUMSS, GAS, Arts & Design, Sports.
TechPro has specializations: ICT, Industrial Arts, Home Economics, Agri-Fishery Arts.
A "doorway option" lets a student add a limited number of electives from the other track.
Do not recommend the old 4-strand (STEM/ABM/HUMSS/TVL) model — it no longer exists.
"""

def _generate_with_resilience(prompt: str):
    models_to_try = [
        "gemini-3.5-flash-lite",
        "gemini-3.8-flash"
    ]
    last_error = None
    for model_name in models_to_try:
        try:
            print(f"Attempting model: {model_name}")
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.2,
                    response_mime_type="application/json"
                ),
            )
            if response and response.text:
                return response
        except Exception as e:
            last_error = e
            print(f"Model {model_name} failed: {e}")
            continue
    raise last_error

@app.route("/api/onet-questions", methods=["GET"])
def get_onet_questions():
    return jsonify({
        "questions": ONET_QUESTIONS,
        "attribution": ONET_ATTRIBUTION,
    })

@app.route("/api/generate", methods=["POST"])
def generate():
    if not GEMINI_API_KEY or client is None:
        return jsonify({"error": "server_misconfigured", "message": "Server is missing GEMINI_API_KEY."}), 500

    payload = request.get_json(force=True, silent=True) or {}
    math_grade = payload.get("math_grade")
    sci_grade = payload.get("sci_grade")
    eng_grade = payload.get("eng_grade")
    tle_grade = payload.get("tle_grade")
    tle_track = payload.get("tle_track")
    commerce_interest = payload.get("commerce_interest", False)
    riasec_scores = payload.get("riasec_scores", {})

    total_checked = sum(riasec_scores.values()) if riasec_scores else 0
    if total_checked == 0 or total_checked == 60:
        return jsonify({
            "error": "low_engagement",
            "message": "You selected either none or all 60 items. This profile isn't a reliable read of your real interests."
        }), 400

    prompt = f"""{SYSTEM_CONTEXT}
Analyze this Grade 10 student:
Subject grades (0-100): Math ({math_grade}), Science ({sci_grade}), English ({eng_grade}), TLE ({tle_grade})
Commerce/business interest indicated: {commerce_interest}
TLE specialization interest: {tle_track}
RIASEC interest checklist results (count out of 10 per domain):
{json.dumps(riasec_scores)}

Output ONLY a valid JSON object matching this schema:
{{
  "primary_track": "Academic or TechPro",
  "primary_cluster": "Name of cluster or specialization",
  "primary_rationale": "Brief rationale explanation...",
  "doorway_option": "Optional cross-track elective suggestion",
  "prerequisite_gaps": ["gap 1", "gap 2"],
  "degree_suggestions": ["degree 1", "degree 2"],
  "tesda_suggestions": ["cert 1", "cert 2"],
  "scholarship_suggestions": ["scholarship 1"],
  "career_suggestions": ["career 1", "career 2"],
  "institution_suggestions": ["school 1", "school 2"]
}}"""

    try:
        response = _generate_with_resilience(prompt)
        result = json.loads(response.text.strip())
        return jsonify({"result": result, "scores": riasec_scores})
    except Exception as e:
        error_trace = traceback.format_exc()
        print("Detailed Generation Error:\n", error_trace)
        return jsonify({
            "error": "generation_failed",
            "message": "Something went wrong generating the recommendation.",
            "technical_detail": str(e),
            "traceback": error_trace
        }), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
