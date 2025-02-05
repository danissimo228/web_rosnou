from sqlalchemy.ext.asyncio import AsyncSession
from functools import cached_property
from fastapi.requests import Request
from application.services.user_service import UserService
from application.core.dependencies import get_session
from fastapi import Depends


class Container:
    def __init__(self, request: Request, session=Depends(get_session)) -> None:
        self.request = request
        self.session = session

    @cached_property  # чтобы этот экземпляр не создавался заново при каждом обращении
    def user_service(self) -> UserService:
        return UserService(self.request, self.session)
