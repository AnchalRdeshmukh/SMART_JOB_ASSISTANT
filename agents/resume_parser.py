from utils.extract_text import extract_pdf_text

def parse_resume(uploaded_file):
    uploaded_file.seek(0)
    text = extract_pdf_text(uploaded_file)
    return text.lower()
