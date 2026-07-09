from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.user.routes import api_router
from engine.database import init_db_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db_connection()
    print("Application startup")
    yield
    print("Application shutdown")


app = FastAPI(
    title="Full Stack Practice API",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)