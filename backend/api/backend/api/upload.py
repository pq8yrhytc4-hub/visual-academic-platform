from fastapi import APIRouter, UploadFile
import uuid, os

router = APIRouter()
BASE_PATH = "backend/storage/files"

@router.post("/")
async def upload_file(file: UploadFile):
    file_id = str(uuid.uuid4())
    path = os.path.join(BASE_PATH, file_id + "_" + file.filename)
    with open(path, "wb") as f:
        f.write(await file.read())
    return {"file_id": file_id, "path": path}
