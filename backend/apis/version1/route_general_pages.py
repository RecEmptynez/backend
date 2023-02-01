from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#Router
general_pages_router = APIRouter()

@general_pages_router.get("/")
async def home(request: Request):
    return (HTMLResponse("Hello World!"))