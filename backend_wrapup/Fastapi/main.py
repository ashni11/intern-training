from uuid import UUID
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from Fastapi import crud
from Fastapi.schemas import TaskCreate, TaskUpdate, TaskResponse
from database.database import get_db

app = FastAPI(
    title="Backend Wrapup API",
    version="1.0.0"
)


@app.post(
    "/tasks",
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    try:
        new_task = crud.create_task(db, task)

        return {
            "success": True,
            "message": "Task created successfully",
            "data": new_task
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/tasks")
def get_tasks(
    db: Session = Depends(get_db)
):
    try:
        tasks = crud.get_tasks(db)

        return {
            "success": True,
            "message": "Tasks fetched successfully",
            "data": tasks
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/tasks/{task_id}")
def get_task(
    task_id: UUID,
    db: Session = Depends(get_db)
):
    try:
        task = crud.get_task(db, task_id)

        return {
            "success": True,
            "message": "Task fetched successfully",
            "data": task
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.put("/tasks/{task_id}")
def update_task(
    task_id: UUID,
    task: TaskUpdate,
    db: Session = Depends(get_db)
):
    try:
        updated_task = crud.update_task(db, task_id, task)

        return {
            "success": True,
            "message": "Task updated successfully",
            "data": updated_task
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: UUID,
    db: Session = Depends(get_db)
):
    try:
        crud.delete_task(db, task_id)

        return {
            "success": True,
            "message": "Task deleted successfully"
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )