from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from db.schemas.recipes import RecipeCreate,ShowRecipe,MultRecipesCreate,MultRecipesShow,DeleteRecipe,ShowDeletedRecipe
from db.session import get_db
from db.repository.recipes import create_new_recipe,create_new_mult_recipes,delete_recipe

router = APIRouter()

@router.post("/create_recipe",response_model=ShowRecipe)
def create_recipe(recipe:RecipeCreate,db:Session = Depends(get_db)):
    recipe = create_new_recipe(recipe=recipe,db=db)
    return recipe

@router.post("/create_recipe/batch",response_model=MultRecipesShow)
def create_mult_recipes(recipes:MultRecipesCreate,db:Session = Depends(get_db)):
    recipes = create_new_mult_recipes(recipes=recipes,db=db)
    return MultRecipesShow(recipes=recipes)

@router.post("/delete_recipe",response_model=ShowDeletedRecipe)
def delete_recipe(recipe:DeleteRecipe,db:Session = Depends(get_db)):
    recipe = delete_recipe(recipe=recipe,db=db)
    return recipe
