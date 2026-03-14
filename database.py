from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)

engine = create_async_engine('sqlite+aiosqlite:///todoapp.db')
session_db = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with session_db() as session:
        yield session

class Base(DeclarativeBase):
    pass