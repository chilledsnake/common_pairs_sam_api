from fastapi import APIRouter

from app.api.v1.nordhealth.endpoints import (
    get_common_numbers_pairs_router,
    project_info_router,
)

# Create a router with a prefix and tag
router = APIRouter(prefix="/nordhealth")

router.include_router(project_info_router)
router.include_router(get_common_numbers_pairs_router)
