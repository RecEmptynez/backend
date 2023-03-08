from pydantic import BaseModel
from typing import List

class Search(BaseModel):
    ingredient_names: List[str]

class SearchResult(BaseModel):
    recipe_names: List[str]