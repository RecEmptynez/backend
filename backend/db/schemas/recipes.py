from typing import Optional
from pydantic import BaseModel,EmailStr


#properties required during user creation
class RecipeCreate(BaseModel):
    title : str
    owner : int

class ShowRecipe(BaseModel):
    title : str
    owner : int

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True
