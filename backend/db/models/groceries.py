from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class Grocery(Base):
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String,nullable= False)
    category = Column(String,ForeignKey("category.id"),nullable= False)