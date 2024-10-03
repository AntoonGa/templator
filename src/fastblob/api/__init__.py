"""File: __init__.py | Author: username | date: Sat Oct 1 2024"""

from fastapi import APIRouter

from fastblob.api.blob_manager.endpoint import router as blob_router
from fastblob.api.etl.endpoint import router as process_router

####################################
## FAST API ROUTERS
####################################
# add all your routers endpoints here
router = APIRouter(prefix="/api")
router.include_router(process_router)
router.include_router(blob_router)
