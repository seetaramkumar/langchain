from fastapi import APIRouter
from server.api.codellama import router as codellama_router
from server.api.gpt import router as gpt_router

router = APIRouter()
router.include_router(codellama_router, prefix="/codellama")
router.include_router(gpt_router, prefix="/gpt")
