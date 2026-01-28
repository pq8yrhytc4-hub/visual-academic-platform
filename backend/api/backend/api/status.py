from fastapi import APIRouter
from core.progress import get

router = APIRouter()

@router.get("/{file_id}")
def get_status(file_id: str):
    return get(file_id)
