from sqlalchemy.orm import Session
from db.models.recipe_ingredient import Recipe_ingredient
from sqlalchemy import Select, func
from db.schemas.recipes import ShowRecipe
from db.repository.ingredients import get_ingredient_by_title

def couple_recipe_ingredient(recipe:ShowRecipe,db:Session):
    ingredients = [(get_ingredient_by_title(ingredient[0],db).id,ingredient[1]) for ingredient in recipe.ingredients]
    for ingredient in ingredients:    
        db_recipe_ingredient = Recipe_ingredient(recipe_id=recipe.id, ingredient_id=ingredient[0], importance=ingredient[1])
        db.add(db_recipe_ingredient)
        db.commit()
        db.refresh(db_recipe_ingredient)
    return db_recipe_ingredient

# Gets all the ingredients from a recipe
def get_num_ingredients(recipe,db:Session) -> dict:
    stmt = Select(func.count(Recipe_ingredient.ingredient_id)).select_from(Recipe_ingredient).where(Recipe_ingredient.recipe_id == recipe)
    result = db.execute(stmt).fetchall()
    return result[0][0]