from sqlalchemy.orm import Session
from typing import List
from db.schemas.recipes import RecipeCreate,MultRecipesCreate,DeleteRecipe,ShowDeletedRecipe
from db.models.recipes import Recipe
from sqlalchemy import Delete
from db.schemas.recipes import MultRecipesShow

#creates a new recipe and returns it
def create_new_recipe(recipe:RecipeCreate,db:Session):
    recipe = Recipe(
        title=recipe.title,
        url=recipe.url
    )
    db.add(recipe)
    db.commit() #commit gives the recipe an id
    db.refresh(recipe)
    return recipe

def recipe_delete(recipe:DeleteRecipe,db:Session):
    delete_stmt = Delete(Recipe).where(Recipe.id == recipe.id).returning(Recipe)
    result = db.execute(delete_stmt).fetchall()[0][0]
    id = result.id
    title = result.title
    url = result.url
    db.commit()
    return ShowDeletedRecipe(id=id,title=title, url=url)
    
#creates a list of new recipes and returns them
def create_new_mult_recipes(recipes:MultRecipesCreate,db:Session):
    bulk_insert = [create_new_recipe(recipe=recipe,db=db) for recipe in recipes.recipes]
    return MultRecipesShow(recipes=bulk_insert)
        

