from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer,autoincrement=True,primary_key = True, index=True)
    title = Column(String,nullable= False)
    ingredient_id = Column(Integer,ForeignKey("ingredients.id"),nullable=False)
