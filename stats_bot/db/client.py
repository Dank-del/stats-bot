from sqlalchemy import create_engine
from .models import User, Group, Message, Attachment
from sqlmodel import SQLModel

__all__ = [User, Group, Message, Attachment]

engine = create_engine("sqlite:///database.db", echo=False)
def load_tables():
    SQLModel.metadata.create_all(engine)