from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from db.schemas.recipes import RecipeCreate,ShowRecipe,MultRecipesCreate,MultRecipesShow,DeleteRecipe,ShowDeletedRecipe
from db.session import get_db
from db.repository.recipes import create_new_recipe,create_new_mult_recipes,recipe_delete
from db.repository.ingredients import create_new_ingredients
from db.repository.recipe_ingredient import couple_recipe_ingredient

router = APIRouter()

#endpoint for creating single recipe
@router.post("/create_recipe",response_model=ShowRecipe)
def create_recipe(recipe:RecipeCreate,db:Session = Depends(get_db)):
    recipe = create_new_recipe(recipe=recipe,db=db)
    ingredients = create_new_ingredients(ingredient_titles=recipe.ingredients,db=db)
    test = couple_recipe_ingredient(recipe=recipe,importance=1,db=db)
    print(recipe,ingredients)
    return recipe

#endpoint for creating multiple recipes
@router.post("/create_recipe/batch",response_model=MultRecipesShow)
def create_mult_recipes(recipes:MultRecipesCreate,db:Session = Depends(get_db)):
    recipes = create_new_mult_recipes(recipes=recipes,db=db)
    return recipes

#endpoint for removing recipe
@router.delete("/delete_recipe",response_model=ShowDeletedRecipe)
def delete_recipe(recipe:DeleteRecipe,db:Session = Depends(get_db)):
    recipe = recipe_delete(recipe=recipe,db=db)
    return recipe
