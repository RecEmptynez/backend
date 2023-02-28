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

def create_new_ingredients(ingredient_titles:List[str],db:Session):
    ingredients = []
    for ingredient_title in ingredient_titles:
        if ingredient_in_database(ingredient_title,db):
            select_stmt = Select(Ingredient).where(Ingredient.title == ingredient_title)
            result = db.execute(select_stmt).fetchall()
            ingredients.append(result)
        
        insert_stmt = Insert(Ingredient).values(title=ingredient_title, category_id=1)
        result = db.execute(insert_stmt).fetchall()
        ingredients.append(result)
    return ingredients
#checks if the ingredient is already in the database, returns true if it is
def ingredient_in_database(ingredient_title:str,db:Session):
    get_stmt = Select(Ingredient).where(Ingredient.title == ingredient_title)
    result = db.execute(get_stmt).fetchall()
    db.commit()
    return len(result) > 0