from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class Recipe(Base):
    id = Column(Integer,primary_key = True,autoincrement=True, index=True)
    title = Column(String,nullable= False)
    owner = Column(Integer,ForeignKey("user.id"),unique=True,nullable=False)
