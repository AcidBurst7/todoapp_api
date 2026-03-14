from fastapi import APIRouter
from sqlalchemy import select

from database import engine, Base

from api.dependencies import SessionDep
from models.tasks import Task
from schemas.tasks import TaskSchema

router = APIRouter()

@router.get("/", summary="Главная страница", tags=["Главная"])
async def home(session: SessionDep):
    query = select(Task)
    tasks = await session.execute(query)
    return tasks.scalars().all()

@router.post("/tasks", summary="Добавление задачи", tags=["Действия с задачами"])
async def create_task(task: TaskSchema, session: SessionDep):
    task = Task(text=task.text)
    session.add(task)
    await session.commit()
    
    return {"success": True, "message": "Задача успешно добавлена"}

@router.put("/tasks", summary="Изменение задачи", tags=["Действия с задачами"])
async def update_task(task_id: int, task_schema: TaskSchema, session: SessionDep):
    task = await session.get(Task, task_id)  
    if task:  
        task.text = task_schema.text  
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