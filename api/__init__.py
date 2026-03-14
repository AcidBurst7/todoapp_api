from fastapi import APIRouter

from api.tasks import router as tasks_router

main_router = APIRouter()

main_router.include_router(tasks_router)