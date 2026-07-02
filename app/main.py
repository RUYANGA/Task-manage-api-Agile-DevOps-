from fastapi import FastAPI, HTTPException

from app.models import Task, TaskCreate
from app.tasks import tasks
from app.logger import logger

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Task API"}