from fastapi import APIRouter

from app.api.v1.nordhealth import router as nordhealth_router

router = APIRouter(prefix="/v1", tags=["v1"])

router.include_router(nordhealth_router)
