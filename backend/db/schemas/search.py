from pydantic import BaseModel
from typing import List

class Search(BaseModel):
    ingredient_names: List[str]

class SearchResult(BaseModel):
    recipe_names: dict[str,List[int]]
    class Config():
        orm_mode = True