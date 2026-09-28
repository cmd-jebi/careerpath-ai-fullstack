# data.py

# ---------------------------------------------------------------------------
# O*NET Interest Profiler Short Form (60 items), U.S. Department of Labor,
# Employment and Training Administration (USDOL/ETA), National Center for
# O*NET Development. Verbatim text from the official instrument
# (onetcenter.org/dl_tools/ipsf/Interest_Profiler.pdf).
# Used under the O*NET Tools Developer License:
# https://www.onetcenter.org/license_tools.html
#
# CareerPath AI has modified the response/scoring format and the downstream
# purpose (feeding a DepEd SHS track/cluster matcher). USDOL/ETA has not
# approved, endorsed, or tested these modifications. A formal validation
# study for this adapted purpose/audience has not yet been conducted.
# ---------------------------------------------------------------------------

ONET_ATTRIBUTION = (
    "This application includes information from the O*NET Career "
    "Exploration Tools by the U.S. Department of Labor, Employment and "
    "Training Administration (USDOL/ETA). Used under the O*NET Tools "
    "Developer License (onetcenter.org/license_tools.html). O*NET(R) is a "
    "trademark of USDOL/ETA. CareerPath AI has modified all or some of "
    "this information. USDOL/ETA has not approved, endorsed, or tested "
    "these modifications."
)

ONET_MODIFICATION_NOTICE = (
    "CareerPath AI has modified all of, a portion of, or the purpose of "
    "the O*NET Career Exploration Tools. USDOL/ETA has not approved, "
    "endorsed, or tested these modifications. As such, USDOL/ETA will not "
    "be liable to any third party or end-user for any damages arising out "
    "of or from the use or misuse of the modified O*NET Career Exploration "
    "Tools. A formal validation study for this adapted purpose (DepEd SHS "
    "track/cluster matching) and audience (Filipino Grade 10 completers) "
    "has not yet been conducted — treat results as preliminary and "
    "exploratory pending that study, and always confirm with a licensed "
    "Guidance Counselor."
)

ONET_QUESTIONS = {
    "Realistic": [
        "Build kitchen cabinets",
        "Lay brick or tile",
        "Repair household appliances",
        "Raise fish in a fish hatchery",
        "Assemble electronic parts",
        "Drive a truck to deliver packages to offices and homes",
        "Test the quality of parts before shipment",
        "Repair and install locks",
        "Set up and operate machines to make products",
        "Put out forest fires",
    ],
    "Investigative": [
        "Develop a new medicine",
        "Study ways to reduce water pollution",
        "Conduct chemical experiments",
        "Study the movement of planets",
        "Examine blood samples using a microscope",
        "Investigate the cause of a fire",
        "Develop a way to better predict the weather",
        "Work in a biology lab",
        "Invent a replacement for sugar",
        "Do laboratory tests to identify diseases",
    ],
    "Artistic": [
        "Write books or plays",
        "Play a musical instrument",
        "Compose or arrange music",
        "Draw pictures",
        "Create special effects for movies",
        "Paint sets for plays",
        "Write scripts for movies or television shows",
        "Perform jazz or tap dance",
        "Sing in a band",
        "Edit movies",
    ],
    "Social": [
        "Teach an individual an exercise routine",
        "Help people with personal or emotional problems",
        "Give career guidance to people",
        "Perform rehabilitation therapy",
        "Do volunteer work at a non-profit organization",
        "Teach children how to play sports",
        "Teach sign language to people who are deaf or hard of hearing",
        "Help conduct a group therapy session",
        "Take care of children at a day-care center",
        "Teach a high-school class",
    ],
    "Enterprising": [
        "Buy and sell stocks and bonds",
        "Manage a retail store",
        "Operate a beauty salon or barber shop",
        "Manage a department within a large company",
        "Start your own business",
        "Negotiate business contracts",
        "Represent a client in a lawsuit",
        "Market a new line of clothing",
        "Sell merchandise at a department store",
        "Manage a clothing store",
    ],
    "Conventional": [
        "Develop a spreadsheet using computer software",
        "Proofread records or forms",
        "Install software across computers on a large network",
        "Operate a calculator",
        "Keep shipping and receiving records",
        "Calculate the wages of employees",
        "Inventory supplies using a hand-held computer",
        "Record rent payments",
        "Keep inventory records",
        "Stamp, sort, and distribute mail for an organization",
    ],
}

# ---------------------------------------------------------------------------
# Track / Cluster data aligned to DepEd Memorandum No. 012, s. 2026
# (Strengthened SHS Curriculum). Two tracks only: Academic and Technical
# Professional (TechPro, replacing TVL). Former strands (STEM/ABM/HUMSS/GAS)
# are elective clusters within Academic, not locked-in strands. Arts &
# Design and Sports move from standalone tracks to Academic electives.
# TechPro keeps the same specialization sectors as former TVL.
# ---------------------------------------------------------------------------

SHS_PATHWAYS = {
    # =======================================================================
    # ACADEMIC TRACK CLUSTERS (5 Clusters)
    # =======================================================================
    "ACAD-ARTS-HUMSS": {
        "track": "Academic",
        "cluster_label": "Arts, Social Sciences, and Humanities Cluster",
        "degrees": [
            "AB Communication", "BA Political Science", "BS Psychology",
            "BA Sociology", "Bachelor of Elementary/Secondary Education"
        ],
        "tesda": [
            "Events Management Services NC II", "Social Work Aide Training",
            "Communication & Media Skills Training (TWSP)"
        ],
        "scholarships": [
            "CHED Merit Scholarship Program", "UniFAST Tertiary Education Subsidy",
            "DSWD/LGU Social Work Assistance Grants"
        ],
        "careers": [
            "Community Development Aide", "Media/Content Production Assistant",
            "HR/Admin Assistant", "Teacher's Aide"
        ],
    },
    "ACAD-BUSINESS": {
        "track": "Academic",
        "cluster_label": "Business and Entrepreneurship Cluster",
        "degrees": [
            "BS Accountancy", "BS Business Administration", "BS Entrepreneurship",
            "BS Economics", "BS Office Administration"
        ],
        "tesda": [
            "Bookkeeping NC III", "Financial Management Training (TWSP)",
            "Events Management Services NC II"
        ],
        "scholarships": [
            "CHED Merit Scholarship Program", "TESDA TWSP",
            "LGU-sponsored local scholarship grants"
        ],
        "careers": [
            "Bookkeeping Clerk", "Sales Associate / Account Executive Trainee",
            "Junior Business Analyst", "Administrative Assistant"
        ],
    },
    "ACAD-STEM": {
        "track": "Academic",
        "cluster_label": "Science, Technology, Engineering, and Mathematics (STEM) Cluster",
        "degrees": [
            "BS Computer Science", "BS Civil/Electrical/Mechanical Engineering",
            "BS Nursing", "BS Biology / Medical Technology", "BS Architecture"
        ],
        "tesda": [
            "Computer Systems Servicing NC II", "Electrical Installation & Maintenance NC II",
            "Shielded Metal Arc Welding NC II"
        ],
        "scholarships": [
            "DOST-SEI S&T Undergraduate Scholarship", "CHED Merit Scholarship Program",
            "UniFAST Tertiary Education Subsidy"
        ],
        "careers": [
            "Junior Software Developer", "Engineering Technician",
            "Laboratory Assistant", "Research Aide"
        ],
    },
    "ACAD-SPORTS-WELLNESS": {
        "track": "Academic",
        "cluster_label": "Sports, Health, and Wellness Cluster",
        "degrees": [
            "BS Exercise & Sports Science", "BS Physical Education",
            "BS Sports Management", "BS Physical Therapy"
        ],
        "tesda": [
            "First Aid NC II", "Fitness Training (TWSP)",
            "Events Management Services NC II"
        ],
        "scholarships": [
            "Philippine Sports Commission (PSC) Scholarship",
            "CHED Merit Scholarship Program", "LGU athletic scholarship grants"
        ],
        "careers": [
            "Fitness Program Assistant", "Sports Program Aide",
            "Recreation Officer Trainee", "Physical Education Assistant"
        ],
    },
    "ACAD-FIELD-EXP": {
        "track": "Academic",
        "cluster_label": "Field Experience Cluster",
        "degrees": [
            "Any bachelor's degree requiring contextual fieldwork",
            "BA/BS Liberal Arts", "BS Social Work", "Pre-Law / Pre-Med preparatory programs"
        ],
        "tesda": [
            "Basic ICT Skills Training (TWSP)", "Events Management Services NC II",
            "Bookkeeping NC III"
        ],
        "scholarships": [
            "CHED Merit Scholarship Program", "UniFAST Tertiary Education Subsidy",
            "LGU-sponsored local scholarship grants"
        ],
        "careers": [
            "Field Researcher Assistant", "Administrative Aide",
            "Customer Service Representative", "Project Assistant Trainee"
        ],
    },

    # =======================================================================
    # TECHPRO TRACK CLUSTERS (10 Clusters)
    # =======================================================================
    "TECHPRO-AESTHETIC": {
        "track": "TechPro",
        "cluster_label": "Aesthetic, Wellness, and Human Care Cluster",
        "degrees": ["BS Beauty Care Management", "BS Physical Therapy Aide", "BS Hospitality Management"],
        "tesda": ["Beauty Care NC II", "Wellness Massage NC II", "Hairdressing NC II"],
        "scholarships": ["TESDA TWSP", "LGU Skills Training Grants"],
        "careers": ["Spa/Wellness Therapist", "Hair & Style Assistant", "Personal Care Specialist"],
    },
    "TECHPRO-AGRI-FOOD": {
        "track": "TechPro",
        "cluster_label": "Agri-Fishery Business and Food Innovation Cluster",
        "degrees": ["BS Agriculture", "BS Agribusiness", "BS Food Technology", "BS Fisheries"],
        "tesda": ["Organic Agriculture Production NC II", "Agricultural Crops Production NC II", "Food Processing NC II"],
        "scholarships": ["DA-ATI Agricultural Scholarships", "TESDA TWSP", "CHED Merit Scholarship Program"],
        "careers": ["Agri-Business Technician", "Food Processing Assistant", "Farm Operations Specialist"],
    },
    "TECHPRO-ARTISANRY": {
        "track": "TechPro",
        "cluster_label": "Artisanry and Creative Enterprise Cluster",
        "degrees": ["BS Entrepreneurship", "BS Craft & Material Design", "BS Fine Arts"],
        "tesda": ["Handicraft Maker NC II", "Jewelry Making NC II", "Fashion Design/Dressmaking NC II"],
        "scholarships": ["TESDA TWSP", "DTI-DADA Enterprise Grants"],
        "careers": ["Crafts Specialist", "Artisan Enterprise Assistant", "Product Designer Assistant"],
    },
    "TECHPRO-AUTO": {
        "track": "TechPro",
        "cluster_label": "Automotive and Small Engine Technologies Cluster",
        "degrees": ["BS Automotive Technology", "BS Mechanical Engineering Technology"],
        "tesda": ["Automotive Servicing NC I/II", "Motorcycle/Small Engine Servicing NC II"],
        "scholarships": ["TESDA TWSP", "Private-industry apprenticeship grants"],
        "careers": ["Automotive Service Assistant", "Small Engine Repair Technician", "Fleet Maintenance Aide"],
    },
    "TECHPRO-CONSTRUCTION": {
        "track": "TechPro",
        "cluster_label": "Construction and Building Technologies Cluster",
        "degrees": ["BS Civil Engineering Technology", "BS Construction Management", "BS Architecture"],
        "tesda": ["Carpentry NC II", "Masonry NC II", "Plumbing NC II", "Tile Setting NC II"],
        "scholarships": ["TESDA TWSP", "Industry-sponsored Apprenticeship Grants"],
        "careers": ["Construction Site Assistant", "Junior Carpenter/Mason", "Building Maintenance Technician"],
    },
    "TECHPRO-CREATIVE-MEDIA": {
        "track": "TechPro",
        "cluster_label": "Creative Arts and Design Technologies Cluster",
        "degrees": ["BS Fine Arts", "BS Multimedia Arts", "BS Industrial Design"],
        "tesda": ["Visual Graphic Design NC III", "Photography NC II", "2D/3D Animation NC II"],
        "scholarships": ["CHED Merit Scholarship Program", "NCCA Grants", "TESDA TWSP"],
        "careers": ["Junior Graphic Designer", "Digital Illustrator Aide", "Media Layout Assistant"],
    },
    "TECHPRO-HOSPITALITY": {
        "track": "TechPro",
        "cluster_label": "Hospitality and Tourism Cluster",
        "degrees": ["BS Hospitality Management", "BS Tourism Management"],
        "tesda": ["Cookery NC II", "Bread & Pastry Production NC II", "Housekeeping NC II", "Front Office Services NC II"],
        "scholarships": ["TESDA TWSP", "DOT Tourism Training Grants"],
        "careers": ["Kitchen Assistant", "Hotel Front Desk Staff", "Tour Operations Assistant"],
    },
    "TECHPRO-ICT": {
        "track": "TechPro",
        "cluster_label": "ICT Support and Computer Programming Technologies Cluster",
        "degrees": ["BS Information Technology", "BS Computer Science", "BS Information Systems"],
        "tesda": ["Computer Systems Servicing NC II", "Web Development NC III", "Programming (.NET/Java) NC III"],
        "scholarships": ["TESDA TWSP", "DICT Digital Jobs Programs", "CHED Merit Scholarship Program"],
        "careers": ["IT Support Technician", "Junior Web Developer", "Systems Administrator Aide"],
    },
    "TECHPRO-INDUSTRIAL": {
        "track": "TechPro",
        "cluster_label": "Industrial Technologies Cluster",
        "degrees": ["BS Industrial Technology", "BS Electrical Engineering Technology"],
        "tesda": ["Electrical Installation & Maintenance NC II", "Shielded Metal Arc Welding NC I/II", "Machining NC II"],
        "scholarships": ["TESDA TWSP", "DOST-SEI Technical Scholarships"],
        "careers": ["Electrician Assistant", "Industrial Machinist Aide", "Welding Technician"],
    },
    "TECHPRO-MARITIME": {
        "track": "TechPro",
        "cluster_label": "Maritime Transport Cluster",
        "degrees": ["BS Marine Transportation", "BS Marine Engineering"],
        "tesda": ["Deck Seamanship NC II", "Engine Watchkeeping NC II"],
        "scholarships": ["MARINA/CHED Maritime Scholarships", "Private Maritime Foundation Grants"],
        "careers": ["Junior Seaman Trainee", "Marine Engine Cadet Aide", "Port Operations Staff"],
    },
}

# ---------------------------------------------------------------------------
# Starter institution reference list mapped to the 15 strengthened clusters.
# ---------------------------------------------------------------------------
INSTITUTIONS = {
    # Academic Track
    "ACAD-ARTS-HUMSS": ["Philippine Normal University", "University of the Philippines (multiple campuses)", "Polytechnic University of the Philippines", "State universities and colleges (SUCs) nationwide"],
    "ACAD-BUSINESS": ["Polytechnic University of the Philippines", "University of Santo Tomas", "De La Salle University", "Ateneo de Manila University", "State universities and colleges (SUCs) nationwide"],
    "ACAD-STEM": ["University of the Philippines (multiple campuses)", "Mapua University", "De La Salle University", "Technological University of the Philippines", "State universities and colleges (SUCs) nationwide"],
    "ACAD-SPORTS-WELLNESS": ["University of the Philippines Diliman (Sports Science)", "Polytechnic University of the Philippines", "Philippine Normal University", "State universities and colleges (SUCs) nationwide"],
    "ACAD-FIELD-EXP": ["Polytechnic University of the Philippines", "State universities and colleges (SUCs) nationwide"],

    # TechPro Track
    "TECHPRO-AESTHETIC": ["TESDA Regional Training Centers (nationwide)", "Philippine Women's University"],
    "TECHPRO-AGRI-FOOD": ["Central Luzon State University", "Visayas State University", "University of the Philippines Los Baños", "TESDA Agri-Fishery Training Centers (regional)"],
    "TECHPRO-ARTISANRY": ["Technological University of the Philippines", "TESDA Regional Training Centers (nationwide)"],
    "TECHPRO-AUTO": ["Technological University of the Philippines", "TESDA Regional Training Centers (nationwide)"],
    "TECHPRO-CONSTRUCTION": ["Technological University of the Philippines", "TESDA Regional Training Centers (nationwide)"],
    "TECHPRO-CREATIVE-MEDIA": ["University of the Philippines College of Fine Arts", "Technological University of the Philippines", "De La Salle-College of Saint Benilde"],
    "TECHPRO-HOSPITALITY": ["TESDA Regional Training Centers (nationwide)", "Philippine Women's University", "State universities and colleges (SUCs) nationwide"],
    "TECHPRO-ICT": ["Technological University of the Philippines", "Polytechnic University of the Philippines", "Mapua University", "TESDA Regional Training Centers (nationwide)"],
    "TECHPRO-INDUSTRIAL": ["Technological University of the Philippines", "TESDA Regional Training Centers (nationwide)"],
    "TECHPRO-MARITIME": ["Philippine Merchant Marine Academy (PMMA)", "MAAP (Maritime Academy of Asia and the Pacific)", "NTMA (NYK-TDG Maritime Academy)"],
}
