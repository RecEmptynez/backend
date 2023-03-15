from pydantic import BaseModel
from typing import List

class SearchIngredient(BaseModel):
    ingredient_string: str


class SearchIngredientResult(BaseModel):
    ingredient: list[str]
    class Config():
        orm_mode = True