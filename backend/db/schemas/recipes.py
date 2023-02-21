from typing import Optional, List
from pydantic import BaseModel,Extra


#properties required during user creation
class RecipeCreate(BaseModel):
    title : str
    url : str

class ShowRecipe(BaseModel):
    title : str
    id : int
    url : str

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True

class MultRecipesCreate(BaseModel):
    recipes : List[RecipeCreate]


class MultRecipesShow(BaseModel):
    recipes : List[ShowRecipe]

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True

