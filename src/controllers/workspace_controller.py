from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.workspace_service import get_workspaces
from src.database.database import get_db

router = APIRouter()

@router.get("/workspaces")
async def list_workspaces(db: AsyncSession = Depends(get_db)):
    return await get_workspaces(db)
