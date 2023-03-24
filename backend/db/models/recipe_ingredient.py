from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

#Creates reflection of the table recipe_ingredient in the database
class Recipe_ingredient(Base):
    __tablename__ = "recipe_ingredient"
    id = Column(Integer,primary_key = True,autoincrement=True, index=True)
    importance = Column(Integer, nullable=False)
    recipe_id = Column(Integer,ForeignKey("recipes.id"),nullable= False)
    ingredient_id = Column(Integer,ForeignKey("ingredients.id"),nullable= False)