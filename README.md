Smart Job Application Assistant 

An Agentic AI-powered job application assistant- that analyzes a candidate’s resume against a job description, computes a job-fit score, matches skills, and generates an AI-assisted cover letter.

This project demonstrates Agentic AI workflows, LLM integration, and end-to-end backend + UI development.
-------------------------------------------------------------------------------------------------------


Features

- Resume PDF parsing
- Job description analysis
- Skill matching between resume and JD
- Job fit score calculation
- AI-generated cover letter using Gemini API
- Multi-agent orchestration with LangGraph
- Interactive UI with Streamlit
-------------------------------------------------------------------------------------------------------

Tech Stack

- Language: Python  
- Frameworks: Streamlit, LangGraph  
- AI / LLM: Google Gemini API  
- PDF Parsing: PyMuPDF  
- ML Utilities: Scikit-learn  
- Environment Management: python-dotenv  
- Version Control:Git & GitHub  
-------------------------------------------------------------------------------------------------------
 Project Structure

smart-job-assistant/
│
├── agents/
│   ├── jd_parser.py
│   ├── resume_parser.py
│   ├── skill_matcher.py
│   ├── fit_score.py
│   └── cover_letter.py
│
├── utils/
│   ├── extract_text.py
│   └── constants.py
│
├── app.py           <-- Streamlit main UI
├── langgraph_app.py <-- LangGraph orchestration
├── requirements.txt
└── README.md
-------------------------------------------------------------------------------------------------------
Clone the Repository
```bash
git clone https://github.com/AnchalRdeshmukh/smart-job-assistant.git
cd smart-job-assistant
-------------------------------------------------------------------------------------------------------


