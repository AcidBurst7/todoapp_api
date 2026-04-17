from fastapi import APIRouter
from sqlalchemy import select
from authx import AuthX, AuthXConfig

from database import engine, Base

from app.api.dependencies import SessionDep
from app.models.tasks import Task
from app.schemas.tasks import TaskSchema

router = APIRouter()

# config = AuthXConfig()
# config.JWT_SECRET_KEY = "SECRET_KEY"
# config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
# config.JWT_TOKEN_LOCATION = ["cookies"]


# @router.post("/login")
# def login():
#     ...

@router.get("/tasks", summary="Список задач", tags=["Действия с задачами"])
async def list_tasks(session: SessionDep):
    query = select(Task)
    tasks = await session.execute(query)
    return tasks.scalars().all()

@router.post("/tasks", summary="Добавление задачи", tags=["Действия с задачами"])
async def create_task(task: TaskSchema, session: SessionDep):
    task = Task(text=task.text, done=task.done)
    session.add(task)
    await session.commit()
    
    return {"success": True, "message": "Задача успешно добавлена"}

@router.put("/tasks", summary="Изменение задачи", tags=["Действия с задачами"])
async def update_task(task_id: int, task_schema: TaskSchema, session: SessionDep):
    task = await session.get(Task, task_id)  
    if task:  
        task.text = task_schema.text
        task.done = task_schema.done  
        await session.commit()  

    return {"success": True, "message": "Задача успешно изменена"}

@router.delete("/{task_id}", summary="Удаление задачи", tags=["Действия с задачами"])
async def delete_task(task_id: int, session: SessionDep):
    task = await session.get(Task, task_id) 
    try: 
        if task:  
            await session.delete(task)
        await session.commit()
        return {"success": True}
    except Exception:  
        return {"success": False}

@router.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)