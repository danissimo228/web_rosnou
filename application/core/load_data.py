from application.database.session import async_engine
from application.database.base import metadata


async def load_data() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
