from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.workspace import Workspace
from src.cache.redis_cache import get_cache, set_cache

async def get_workspaces(db: AsyncSession):
    cache_result = get_cache("workspaces")
    if cache_result:
        return cache_result  # Retorna desde la caché si está disponible

    result = await db.execute(select(Workspace))
    workspaces = result.scalars().all()

    set_cache("workspaces", workspaces, expiration=120)
    return workspaces
