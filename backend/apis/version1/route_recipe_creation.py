from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.schemas.recipes import RecipeCreate,ShowRecipe,MultRecipesCreate,MultRecipesShow,DeleteRecipe,ShowDeletedRecipe
from db.session import get_db
from db.repository.recipes import create_new_recipe,recipe_delete
from db.repository.ingredients import create_new_ingredients
from db.repository.recipe_ingredient import couple_recipe_ingredient
from fastapi import responses

router = APIRouter()

#endpoint for creating single recipe
@router.post("/create_recipe",response_model=ShowRecipe)
def create_recipe(recipe:RecipeCreate,db:Session = Depends(get_db)):
    recipe = create_new_recipe(recipe=recipe,db=db)
    create_new_ingredients(ingredient_titles=recipe.ingredients,db=db)
    couple_recipe_ingredient(recipe=recipe,db=db)
    return recipe

#endpoint for creating multiple recipes
@router.post("/create_recipe/batch",status_code=201)
def create_mult_recipes(recipes:MultRecipesCreate,db:Session = Depends(get_db)):
    for recipe in recipes.recipes:
        create_recipe(recipe, db)
    return responses.HTMLResponse(status_code=201)

#endpoint for removing recipe
@router.delete("/delete_recipe",response_model=ShowDeletedRecipe)
def delete_recipe(recipe:DeleteRecipe,db:Session = Depends(get_db)):
    recipe = recipe_delete(recipe=recipe,db=db)
    return recipe
