import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_cover_letter(role, skills):
    skills_text = ", ".join(skills) if skills else "relevant technical skills"

    prompt = f"""
    Write a professional cover letter for the role of {role}.

    Candidate skills:
    {skills_text}

    Keep the tone professional and concise.
    """

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return response.text
