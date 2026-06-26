from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database.models import Task
from Fastapi.schemas import TaskCreate, TaskUpdate

def create_task(db: Session, task: TaskCreate):
    try:
        new_task = Task(
            title=task.title,
            message=task.message,
            completed=task.completed
        )

        db.add(new_task)
        db.commit()
        db.refresh(new_task)

        return new_task

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating task: {str(e)}"
        )


def get_tasks(db: Session):
    try:
        return db.query(Task).filter(Task.is_deleted == False).all()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching tasks: {str(e)}"
        )


def get_task(db: Session, task_id):
    try:
        task = db.query(Task).filter(
            Task.id == task_id,
            Task.is_deleted == False
        ).first()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        return task

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching task: {str(e)}"
        )


def update_task(db: Session, task_id, updated_task: TaskUpdate):
    try:
        task = db.query(Task).filter(
            Task.id == task_id,
            Task.is_deleted == False
        ).first()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        task.title = updated_task.title
        task.message = updated_task.message
        task.completed = updated_task.completed

        db.commit()
        db.refresh(task)

        return task

    except HTTPException:
        raise

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating task: {str(e)}"
        )


def delete_task(db: Session, task_id):
    try:
        task = db.query(Task).filter(
            Task.id == task_id,
            Task.is_deleted == False
        ).first()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        # Soft Delete
        task.is_deleted = True

        db.commit()

        return {
            "message": "Task deleted successfully"
        }

    except HTTPException:
        raise

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting task: {str(e)}"
        )