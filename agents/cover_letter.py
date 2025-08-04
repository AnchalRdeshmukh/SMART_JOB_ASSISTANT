from utils.constants import COVER_LETTER_TEMPLATE

def generate_cover_letter(candidate, company, role, skills, hiring_manager="Hiring Manager"):
    return COVER_LETTER_TEMPLATE.format(
        candidate=candidate,
        company=company,
        role=role,
        skills=", ".join(skills),
        hiring_manager=hiring_manager
    )

