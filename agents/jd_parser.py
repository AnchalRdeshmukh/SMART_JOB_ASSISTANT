import re

def parse_job_description(jd_text):
    sections = {
        "Responsibilities": r"(Responsibilities|Job Responsibilities|Duties)[\s\S]*?(?=\n[A-Z]|$)",
        "Qualifications": r"(Qualifications|Requirements|Must Have)[\s\S]*?(?=\n[A-Z]|$)",
        "Skills": r"(Skills Required|Technical Skills|Skills)[\s\S]*?(?=\n[A-Z]|$)"
    }

    extracted = {}
    for section, pattern in sections.items():
        match = re.search(pattern, jd_text, re.IGNORECASE)
        if match:
            extracted[section] = match.group(0).strip()
        else:
            extracted[section] = "Not Found"
    return extracted
