from pdfminer.high_level import extract_text
from docx import Document

def extract_raw_text(path):
    if path.endswith(".pdf"):
        return extract_text(path)
    elif path.endswith(".docx"):
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs)
    else:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
