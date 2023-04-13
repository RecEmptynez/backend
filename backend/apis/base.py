from fastapi import APIRouter

from apis.version1 import route_general_pages
from apis.version1 import route_recipe_creation
from apis.version1 import route_search
from apis.version1 import route_search_ingredient

api_router = APIRouter()
api_router.include_router(route_general_pages.general_pages_router,prefix="",tags=["general_pages"])
api_router.include_router(route_recipe_creation.router,prefix="/recipes",tags=["recipes"])
api_router.include_router(route_search.router,prefix="/search",tags=["search"])
api_router.include_router(route_search_ingredient.router, prefix="/search", tags=["search"])