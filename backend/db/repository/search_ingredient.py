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


def search_ingredient(search_ingedient:SearchIngredient , db:Session):
    #stmt = 

    return 0