from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from app.api import router as api_router
from app.config import env_vars

root_path = f"/{env_vars.APP_ENV}" if env_vars.APP_ENV != "local" else ""

app = FastAPI(
    title="nordhealth-api.ownspace.cloud API",
    description="nordhealth-api.ownspace.cloud API",
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

handler = Mangum(app)
