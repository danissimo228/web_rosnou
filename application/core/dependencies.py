from application.database.session import AsyncSessionLocal


async def get_session():
    """
    Зависимость для создания сессии и открытия транзакции в контексте корутины обрабатывающей запрос

    :rtype: AsyncSession
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            yield session
