from fastapi import APIRouter
from core.extractor import extract_raw_text
from core.sectionizer import split_sections
from core.sentence_splitter import split_sentences
from core.progress import update

router = APIRouter()

@router.post("/{file_id}")
def process_file(file_id: str, path: str):
    update(file_id, "Extracting text", 30)
    text = extract_raw_text(path)

    update(file_id, "Sectionizing", 60)
    sections = split_sections(text)

    update(file_id, "Done", 100)
    return sections
