from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.schemas.search import Search 
from db.session import get_db
from db.repository.search import search_recipe
from db.schemas.search import SearchResult

router = APIRouter()

@router.post("/recipes",response_model=SearchResult)
def search_recipes(search:Search, db:Session=Depends(get_db)):
    recipes = search_recipe(search,db)
    return recipes