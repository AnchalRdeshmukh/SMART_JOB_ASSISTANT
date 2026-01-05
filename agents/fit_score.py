def calculate_fit(matched, jd_skills):
    if not jd_skills:
        return 0
    return round((len(matched) / len(jd_skills)) * 100, 2)
