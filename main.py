from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware after creating the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production, e.g., ["http://example.com"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods like GET, POST, PUT, DELETE
    allow_headers=["*"],  # Allows all headers
)

class TaskInput(BaseModel):
    task: str

@app.post("/submit")
async def receive_task(task_input: TaskInput):
    return {"received_task": task_input.task}