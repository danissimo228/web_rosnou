import uuid
from application.database.base import Base
from sqlalchemy import Column, String


class User(Base):
    __tablename__ = "user"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    password = Column(String(10), nullable=False)
    username = Column(String(10), unique=True, nullable=False)
    email = Column(String(20), unique=True, nullable=False)
