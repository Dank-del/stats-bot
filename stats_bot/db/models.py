from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: Optional[str] = Field(nullable=True)
    first_name: str
    last_name: Optional[str] = Field(nullable=True)

class Group(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    username: Optional[str] = Field(nullable=True)
    type: str
    members: int

class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    group_id: int = Field(foreign_key="group.id")
    text: str
    timestamp: datetime = Field(default=datetime.utcnow)
