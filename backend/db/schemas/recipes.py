from typing import Optional, List
from pydantic import BaseModel,EmailStr


#properties required during user creation
class RecipeCreate(BaseModel):
    title : str

class ShowRecipe(BaseModel):
    title : str
    id : int

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
    
    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True