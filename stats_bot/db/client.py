from sqlalchemy import create_engine
from . import models
from sqlmodel import SQLModel

engine = create_engine("sqlite:///database.db", echo=False)
def load_tables():
    SQLModel.metadata.create_all(engine, tables=[models.User.__table__, models.Group.__table__, models.Message.__table__])