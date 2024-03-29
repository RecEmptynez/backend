from sqlalchemy.orm import Session
from db.models.recipes import Recipe
from db.schemas.search import Search
from db.models.ingredients import Ingredient
from db.models.recipe_ingredient import Recipe_ingredient
from sqlalchemy import Select, distinct, desc, or_
from db.schemas.search import SearchResult
from db.repository.recipe_ingredient import get_num_ingredients
from sqlalchemy import func

def search_recipe(search:Search,db:Session):
    limit = search.max_num
    # create the dynamic WHERE clause
    where_clause = or_(*[Ingredient.title.ilike(f'%{search_term}%') for search_term in search.ingredient_names])
    
    count_function = func.count(distinct(Recipe_ingredient.ingredient_id))
    sorting_function = (Recipe_ingredient.importance*func.count(distinct(Recipe_ingredient.ingredient_id)))

    stmt = Select(
                    distinct(Recipe.title), 
                    Recipe.id, 
                    Recipe.url, 
                    Recipe.picture_url, 
                    Recipe.difficulty, 
                    Recipe.rating, 
                    count_function.label('ingredient_count'), 
                    sorting_function.label("sorting")).select_from(Recipe).join(
                        Recipe_ingredient, 
                        Recipe.id == Recipe_ingredient.recipe_id).join(
                        Ingredient, 
                        Ingredient.id == Recipe_ingredient.ingredient_id).where(where_clause).group_by(
                            Recipe.title, 
                            Recipe.id, 
                            Recipe.url, 
                            Recipe_ingredient.importance, 
                            Recipe.picture_url, 
                            Recipe.difficulty, 
                            Recipe.rating).order_by(desc('sorting')).limit(limit)
    
    result = db.execute(stmt).fetchall()
    return SearchResult(recipe_names={recipe[0]: 
                                      {"owned":recipe[6] if search.ingredient_names else 0 ,
                                       "total":get_num_ingredients(recipe[1],db),"url":recipe[2], 
                                       "picture_url":recipe[3], 
                                       "difficulty":int(recipe[4]), 
                                       "rating":float(recipe[5])} 
                                       for recipe in result})