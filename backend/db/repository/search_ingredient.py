from sqlalchemy.orm import Session
from db.schemas.search_ingredient import SearchIngredient
from db.models.ingredients import Ingredient
from sqlalchemy import Select



def search_ingredient(search_ingredient:SearchIngredient , db:Session):
    search_str = search_ingredient.ingredient_string
    stmt = Select(Ingredient.title).where(Ingredient.title.like(f'{search_str}%'))
    results = db.execute(stmt).fetchall()
    returns = []
    for result in results:
        returns.append(result[0])
    return returns
