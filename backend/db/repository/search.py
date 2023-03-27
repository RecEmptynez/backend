from sqlalchemy.orm import Session
from db.schemas.recipes import RecipeCreate,DeleteRecipe,ShowDeletedRecipe,ShowRecipe
from db.models.recipes import Recipe
from db.schemas.search import Search
from db.models.categories import Category
from db.models.ingredients import Ingredient
from db.models.recipe_ingredient import Recipe_ingredient
from sqlalchemy import Delete, Insert, Select, Join, distinct, desc, or_, text
from db.schemas.search import SearchResult
from db.repository.recipe_ingredient import get_num_ingredients
import re
from sqlalchemy import func

def search_recipe(search:Search,db:Session):
    limit = search.count
    # create the dynamic WHERE clause
    where_clause = or_(*[Ingredient.title.ilike(f'%{search_term}%') for search_term in search.ingredient_names])
    stmt = Select(distinct(Recipe.title), Recipe.id, Recipe.url, Recipe.picture_url, Recipe.difficulty, Recipe.rating, func.count(distinct(Recipe_ingredient.ingredient_id)).label('ingredient_count'), (Recipe_ingredient.importance*func.count(distinct(Recipe_ingredient.ingredient_id))).label("sorting")).select_from(Recipe).join(Recipe_ingredient, Recipe.id == Recipe_ingredient.recipe_id).join(Ingredient, Ingredient.id == Recipe_ingredient.ingredient_id).where(where_clause).group_by(Recipe.title, Recipe.id, Recipe.url, Recipe_ingredient.importance, Recipe.picture_url, Recipe.difficulty, Recipe.rating).order_by(desc('sorting')).limit(limit)
    result = db.execute(stmt).fetchall()
    return SearchResult(recipe_names={recipe[0]: {"owned":recipe[6],"total":get_num_ingredients(recipe[1],db),"url":recipe[2], "picture_url":recipe[3], "difficulty":recipe[4], "rating":recipe[5]} for recipe in result})