from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

tasks = []
class TaskCreate(BaseModel):
    title: str
    completed: bool = False
    message:str
class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
app = FastAPI()
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks)+1,
        "title": task.title,
        "completed": task.completed
    }
    tasks.append(new_task)
    return new_task
@app.get("/tasks/{id}")
def get_task(id:int):

    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(404,"Task not found")


@app.put("/tasks/{id}")
def update_task(id:int, updated_task:TaskCreate):

    for task in tasks:

        if task["id"] == id:
            task["title"] = updated_task.title
            task["completed"] = updated_task.completed
            return task

    raise HTTPException(404,"Task not found")
@app.delete("/tasks/{id}")
def delete_task(id:int):

    for task in tasks:

        if task["id"] == id:
            tasks.remove(task)
            return {"message":"Task deleted"}

    raise HTTPException(404,"Task not found")

