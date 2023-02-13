from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class Category(Base):
    id = Column(Integer,primary_key = True, index=True)
    name = Column(String,nullable= False, primary_key=True)
    priority = Column(Integer,nullable= False)
    user_id = Column(Integer,ForeignKey("user.id"),unique=True,nullable=False)
