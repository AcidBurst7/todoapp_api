from datetime import datetime
from typing import Annotated

from fastapi import FastAPI, Depends
# import uvicorn
from sqlalchemy import select
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

from models.base import Base
from models.task import Task
from schemas.task import TaskSchema

app = FastAPI()
engine = create_async_engine('sqlite+aiosqlite:///todoapp.db')
session_db = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with session_db() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]


@app.get("/", summary="Главная страница", tags=["Главная"])
async def home(session: SessionDep):
    query = select(Task)
    tasks = await session.execute(query)
    return tasks.scalars().all()

@app.post("/tasks", summary="Добавление задачи", tags=["Действия с задачами"])
async def create_task(task: TaskSchema, session: SessionDep):
    task = Task(text=task.text)
    session.add(task)
    await session.commit()
    
    return {"success": True, "message": "Книга успешно добавлена"}

@app.put("/tasks", summary="Изменение задачи", tags=["Действия с задачами"])
async def update_task(task_id: int, task_schema: TaskSchema, session: SessionDep):
    task = await session.get(Task, task_id)  
    if task:  
        task.text = task_schema.text  
        await session.commit()  

    return {"success": True, "message": "Книга успешно изменена"}

@app.delete("/{task_id}", summary="Удаление задачи", tags=["Действия с задачами"])
async def delete_task(task_id: int, session: SessionDep):
    task = await session.get(Task, task_id) 
    try: 
        if task:  
            await session.delete(task)
        await session.commit()
        return {"success": True}
    except Exception:  
        return {"success": False}

@app.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

# if __name__ == '__main__':
#     uvicorn.run("main:app", reload=True)
