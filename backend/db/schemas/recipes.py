from typing import Optional, List
from pydantic import BaseModel,EmailStr,Extra


#properties required during user creation
class RecipeCreate(BaseModel):
    title : str
    url : str
    difficulty: str
    picture_url: str
    rating: str
    ingredients: List[List[str]]

class ShowRecipe(BaseModel):
    title : str
    id : int
    url : str
    difficulty: str
    ingredients: List[List[str]]

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True

class MultRecipesCreate(BaseModel):
    recipes : List[RecipeCreate]

class MultRecipesShow(BaseModel):
    recipes : List[ShowRecipe]

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True

class DeleteRecipe(BaseModel):
    id : int

class ShowDeletedRecipe(BaseModel):
    title : str
    id : int
    url: str
    difficulty: str    
    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True
