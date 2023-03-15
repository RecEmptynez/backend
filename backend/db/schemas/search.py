from pydantic import BaseModel
from typing import List

class Search(BaseModel):
    ingredient_names: dict[str]

class SearchResult(BaseModel):
    recipe_names: dict[str,List[float]]
    class Config():
        orm_mode = True