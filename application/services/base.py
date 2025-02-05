from typing import Optional
from starlette.requests import Request


class Service:
    def __init__(self, request: Optional[Request], session) -> None:
        self.request = request
        self.session = session
