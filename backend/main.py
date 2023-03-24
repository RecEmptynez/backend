from fastapi import FastAPI
from core.config import settings
from apis.base import api_router
from db.session import engine  
from db.Base import Base 
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
]

def create_tables():  
    print("Creating tables")        
    Base.metadata.create_all(bind=engine)

def include_router(app):
	app.include_router(api_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    include_router(app)
    app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
    create_tables()
    return app 

app = start_application()