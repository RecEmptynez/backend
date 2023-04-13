from sqlalchemy.orm import Session
from typing import List
from db.models.ingredients import Ingredient
from sqlalchemy import Select
from sqlalchemy import Insert

#inserts ingredients into the database and couples them with a category TODO implement categories
def create_new_ingredients(ingredient_titles:List[List[str]],db:Session):
    ingredients = []
    for ingredient_info in ingredient_titles:
        ingredient_title = ingredient_info[0]
        if ingredient_in_database(ingredient_title,db):
            select_stmt = Select(Ingredient).where(Ingredient.title == ingredient_title)
            result = db.execute(select_stmt).fetchall()
            ingredients.append((result[0][0].id,result[0][0].title,result[0][0].category_id))
        else:
            insert_stmt = Insert(Ingredient).values(title=ingredient_title, category_id=1).returning(Ingredient.id,Ingredient.title,Ingredient.category_id)
            result = db.execute(insert_stmt).fetchall()
            db.commit()
            ingredients.append(result[0])
    
    return ingredients
#checks if the ingredient is already in the database, returns true if it is
def ingredient_in_database(ingredient_title:str,db:Session):
    get_stmt = Select(Ingredient).where(Ingredient.title == ingredient_title)
    result = db.execute(get_stmt).fetchall()
    db.commit()
    return len(result) > 0

#returns the ingredient object from the database
def get_ingredient_by_title(ingredient_title:str,db:Session):
    get_stmt = Select(Ingredient).where(Ingredient.title == ingredient_title)
    result = db.execute(get_stmt).fetchall()
    db.commit()
    return result[0][0]