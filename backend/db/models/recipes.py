from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer,primary_key = True,autoincrement=True, index=True)
    title = Column(String,nullable= False)

