from sqlalchemy.orm import Session
from db.schemas.recipes import RecipeCreate,DeleteRecipe,ShowDeletedRecipe,ShowRecipe
from db.models.recipes import Recipe
from db.models.categories import Category
from sqlalchemy import Delete, Insert

#creates a new recipe and returns it
def create_new_recipe(recipe:RecipeCreate,db:Session):
    #Create the recipe:
    db_recipe = Recipe(title=recipe.title, url=recipe.url, difficulty=recipe.difficulty)    
    db.add(db_recipe)
    db.commit() #commit gives the recipe an id
    db.refresh(db_recipe)
    return ShowRecipe(id=db_recipe.id,title=db_recipe.title,url=db_recipe.url,ingredients=recipe.ingredients, difficulty=recipe.difficulty)

def recipe_delete(recipe:DeleteRecipe,db:Session):
    delete_stmt = Delete(Recipe).where(Recipe.id == recipe.id).returning(Recipe)
    result = db.execute(delete_stmt).fetchall()[0][0]
    id = result.id
    title = result.title
    url = result.url
    difficulty = result.difficulty
    db.commit()
    return ShowDeletedRecipe(id=id,title=title, url=url, difficulty=difficulty)


        

