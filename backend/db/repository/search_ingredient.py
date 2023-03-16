from sqlalchemy.orm import Session
from db.schemas.recipes import RecipeCreate,DeleteRecipe,ShowDeletedRecipe,ShowRecipe
from db.schemas.search_ingredient import SearchIngredient
from db.models.recipes import Recipe
from db.schemas.search import Search
from db.models.categories import Category
from db.models.ingredients import Ingredient
from db.models.recipe_ingredient import Recipe_ingredient
from sqlalchemy import Delete, Insert, Select, Join, distinct
from db.schemas.search import SearchResult
from db.repository.recipe_ingredient import get_ingredients_from_recipe
#from models.ingredients import Ingredient


def search_ingredient(search_ingredient:SearchIngredient , db:Session):
    search_str = search_ingredient.ingredient_string
    print(search_str)
    stmt = Select(Ingredient.title).where(Ingredient.title.like(f'{search_str}%'))
    print(stmt)
    results = db.execute(stmt).fetchall()
    returns = []
    for result in results:
        returns.append(result[0])
        print(result[0]) 
    print(returns)
    return returns