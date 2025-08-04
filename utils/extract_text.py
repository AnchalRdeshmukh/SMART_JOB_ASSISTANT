import re
from docx import Document
import fitz  # PyMuPDF for PDF processing

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file-like object using PyMuPDF."""
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return clean_text(text)

def extract_text_from_docx(docx_file):
    """Extract text from a DOCX file-like object using python-docx."""
    doc = Document(docx_file)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return clean_text(text)

def parse_resume(file):
    """Detect file type and parse resume accordingly."""
    file_extension = file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        return extract_text_from_pdf(file)
    elif file_extension == 'docx':
        return extract_text_from_docx(file)
    else:
        return "Unsupported file format"

def clean_text(text):
    """Clean and normalize text by removing extra whitespaces."""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
