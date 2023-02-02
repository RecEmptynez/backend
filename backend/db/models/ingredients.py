from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class Ingredient(Base):
    recipe_id = Column(Integer,ForeignKey("recipe.id"),primary_key=True,nullable=False)
    grocery_id = Column(Integer,ForeignKey("grocery.id"),primary_key=True,nullable=False)
    quantity = Column(Integer,nullable=True)
    unit = Column(String,nullable=True)
    instruction = Column(String,nullable=True)
