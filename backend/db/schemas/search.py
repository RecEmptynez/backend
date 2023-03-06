from pydantic import BaseModel
from typing import List

class Search(BaseModel):
    ingredient_names: List[str]
