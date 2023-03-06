from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.schemas.recipes import RecipeCreate,ShowRecipe,MultRecipesCreate,MultRecipesShow,DeleteRecipe,ShowDeletedRecipe
from db.session import get_db
from db.repository.recipes import create_new_recipe,recipe_delete
from db.repository.ingredients import create_new_ingredients
from db.repository.recipe_ingredient import couple_recipe_ingredient

router = APIRouter()

