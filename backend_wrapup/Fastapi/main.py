from uuid import UUID
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from Fastapi import crud
from Fastapi.schemas import TaskCreate, TaskUpdate
from database.database import get_db
app = FastAPI(
    title="Backend Wrapup API",
    version="1.0.0"
)
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    try:
        new_task = crud.create_task(db, task)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": True,
                "message": "Task created successfully",
                "data": {
                    "id": str(new_task.id),
                    "title": new_task.title,
                    "message": new_task.message,
                    "completed": new_task.completed,
                    "created_at": str(new_task.created_at),
                    "created_by": new_task.created_by,
                    "updated_at": str(new_task.updated_at),
                    "updated_by": new_task.updated_by,
                    "is_active": new_task.is_active,
                    "is_deleted": new_task.is_deleted
                }
            }
        )
    except HTTPException:
        raise
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": str(e)
            }
        )
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    try:
        tasks = crud.get_tasks(db)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "message": "Tasks fetched successfully",
                "data": [
                    {
                        "id": str(task.id),
                        "title": task.title,
                        "message": task.message,
                        "completed": task.completed,
                        "created_at": str(task.created_at),
                        "created_by": task.created_by,
                        "updated_at": str(task.updated_at),
                        "updated_by": task.updated_by,
                        "is_active": task.is_active,
                        "is_deleted": task.is_deleted
                    }
                    for task in tasks
                ]
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": str(e)
            }
        )
@app.get("/tasks/{task_id}")
def get_task(task_id: UUID, db: Session = Depends(get_db)):
    try:
        task = crud.get_task(db, task_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "message": "Task fetched successfully",
                "data": {
                    "id": str(task.id),
                    "title": task.title,
                    "message": task.message,
                    "completed": task.completed,
                    "created_at": str(task.created_at),
                    "created_by": task.created_by,
                    "updated_at": str(task.updated_at),
                    "updated_by": task.updated_by,
                    "is_active": task.is_active,
                    "is_deleted": task.is_deleted
                }
            }
        )
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "message": e.detail
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": str(e)
            }
        )
@app.put("/tasks/{task_id}")
def update_task(
    task_id: UUID,
    task: TaskUpdate,
    db: Session = Depends(get_db)
):
    try:
        updated_task = crud.update_task(db, task_id, task)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "message": "Task updated successfully",
                "data": {
                    "id": str(updated_task.id),
                    "title": updated_task.title,
                    "message": updated_task.message,
                    "completed": updated_task.completed,
                    "created_at": str(updated_task.created_at),
                    "created_by": updated_task.created_by,
                    "updated_at": str(updated_task.updated_at),
                    "updated_by": updated_task.updated_by,
                    "is_active": updated_task.is_active,
                    "is_deleted": updated_task.is_deleted
                }
            }
        )

    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "message": e.detail
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": str(e)
            }
        )


@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID, db: Session = Depends(get_db)):
    try:
        crud.delete_task(db, task_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "message": "Task deleted successfully"
            }
        )

    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "message": e.detail
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": str(e)
            }
        )