import fitz  # PyMuPDF

def extract_pdf_text(uploaded_file):
    text = ""

    # Streamlit UploadedFile → bytes
    pdf_bytes = uploaded_file.read()

    # Open PDF from bytes
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    for page in doc:
        text += page.get_text()

    return text
