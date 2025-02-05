from asyncio import current_task

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

db_url = "sqlite+aiosqlite:///test.db"
engine = create_engine(db_url)
async_engine = create_async_engine(db_url)
async_session = sessionmaker(bind=async_engine, class_=AsyncSession, future=True)
AsyncSessionLocal = async_scoped_session(async_session, scopefunc=current_task)
