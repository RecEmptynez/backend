from pydantic import BaseModel


#properties required during user creation
class CreateIngredient(BaseModel):
    title : str

class ShowIngredient(BaseModel):
    title : str

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True
