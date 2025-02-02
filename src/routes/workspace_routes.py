from fastapi import APIRouter
from src.controllers.workspace_controller import router as workspace_router

router = APIRouter()

router.include_router(workspace_router, prefix="/api", tags=["Workspaces"])
