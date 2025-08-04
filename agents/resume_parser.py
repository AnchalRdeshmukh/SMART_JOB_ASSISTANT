import fitz  # PyMuPDF
import re
from docx import Document
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def parse_resume(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext == ".docx":
        text = extract_text_from_docx(file_path)
    else:
        return "Unsupported file format"

    return extract_sections(text)

def extract_sections(text):
    sections = {
        "Experience": r"(Experience|Work History|Employment)[\s\S]*?(?=\n[A-Z]|$)",
        "Education": r"(Education|Qualifications)[\s\S]*?(?=\n[A-Z]|$)",
        "Skills": r"(Skills|Technical Skills)[\s\S]*?(?=\n[A-Z]|$)"
    }

    extracted = {}
    for key, pattern in sections.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            extracted[key] = match.group(0).strip()
        else:
            extracted[key] = "Not Found"
    return extracted
