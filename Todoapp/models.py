from database import Base
from sqlalchemy import Boolean, Column , Integer , String, true
class Todos(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key = True, index= True)
    title = Column(String)
    description = Column(String)
    complete = Column(Boolean, default=False)

