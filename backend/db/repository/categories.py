from sqlalchemy.orm import Session
from typing import List
from db.schemas.recipes import RecipeCreate,MultRecipesCreate,DeleteRecipe,ShowDeletedRecipe
from db.models.recipes import Recipe
from db.models.recipe_ingredient import Recipe_ingredient
from db.models.ingredients import Ingredient
from sqlalchemy import Delete
from sqlalchemy import Select
from sqlalchemy import Insert
from db.schemas.recipes import MultRecipesShow
from db.models.categories import Category

def insert_category(category_name:str,db:Session):
    insert_stmt = Insert(Category).values(title=category_name).returning(Category.id,Category.title)
    result = db.execute(insert_stmt).fetchall()
    db.commit()
    return result[0]