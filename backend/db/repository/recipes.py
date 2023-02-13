from sqlalchemy.orm import Session

from db.schemas.recipes import RecipeCreate
from db.models.recipes import Recipe

def create_new_recipe(recipe:RecipeCreate,db:Session):
    recipe = Recipe(
        title=recipe.title,
        owner=recipe.owner
    )
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe