from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from db.schemas.recipes import RecipeCreate,ShowRecipe
from db.session import get_db
from db.repository.recipes import create_new_recipe

router = APIRouter()

@router.post("/",response_model=ShowRecipe)
def create_recipe(recipe:RecipeCreate,db:Session = Depends(get_db)):
    recipe = create_new_recipe(recipe=recipe,db=db)
    return recipe