from pydantic import BaseModel
from typing import List,Any

class Search(BaseModel):
    count : int
    ingredient_names: List[str]

class SearchResult(BaseModel):
    recipe_names: dict[str,dict[str,Any]]
    class Config():
        orm_mode = True