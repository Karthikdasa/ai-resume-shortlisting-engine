import fitz  # PyMuPDF
import docx2txt


def extract_text(file_path):
    """
    Extract text from PDF or DOCX file.
    """
    if file_path.lower().endswith(".pdf"):
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text

    elif file_path.lower().endswith(".docx"):
        return docx2txt.process(file_path)

    return ""