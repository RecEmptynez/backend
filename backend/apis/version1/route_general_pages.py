from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse,RedirectResponse

#Router
general_pages_router = APIRouter()

@general_pages_router.get("/")
async def home(request: Request):
    return (RedirectResponse(url="/docs"))
