from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String,nullable= False)
    category_id = Column(String,ForeignKey("categories.id"),nullable= False)
