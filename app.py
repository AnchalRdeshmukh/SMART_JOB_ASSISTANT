import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-pro-latest")

app = Flask(__name__)

@app.route("/")
def home():
    return "Gemini AI Resume Assistant is running!"

# 1. Resume-Job Matching Score
@app.route("/match", methods=["POST"])
def match_resume_to_job():
    data = request.json
    resume = data.get("resume", "")
    job_description = data.get("job_description", "")

    prompt = f"""
You are an expert HR AI system.

Compare the following resume and job description and give a semantic match score from 0 to 100, along with a short reason.

Resume:
{resume}

Job Description:
{job_description}

Respond with JSON like:
{{
  "score": 88,
  "reason": "Strong match in required skills such as Python, data pipelines, and cloud experience."
}}
    """

    try:
        response = model.generate_content(prompt)
        return jsonify(json.loads(response.text.strip()))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 2. Cover Letter Generation
@app.route("/cover_letter", methods=["POST"])
def generate_cover_letter():
    data = request.json
    resume = data.get("resume", "")
    job_description = data.get("job_description", "")
    name = data.get("name", "Candidate")

    prompt = f"""
Generate a professional and tailored cover letter for the following person applying to the given job.

Name: {name}

Resume:
{resume}

Job Description:
{job_description}

Format the letter properly and make it compelling. Avoid repetition and generic language.
    """

    try:
        response = model.generate_content(prompt)
        return jsonify({"cover_letter": response.text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
