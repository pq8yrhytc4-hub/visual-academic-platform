from fastapi import FastAPI
from api import upload, process, status

app = FastAPI(title="Visual Academic Platform")

app.include_router(upload.router, prefix="/upload")
app.include_router(process.router, prefix="/process")
app.include_router(status.router, prefix="/status")
