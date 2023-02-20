from typing import Optional
from pydantic import BaseModel,EmailStr


#properties required during user creation
class CreateCategory(BaseModel):
    title : str

class ShowCategory(BaseModel):
    title : str

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True
