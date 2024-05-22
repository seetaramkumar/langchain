from fastapi import APIRouter, Request
from models.codellama import load_codellama_model, generate_codellama_response
from config import MODELS
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    router = APIRouter()
    model, tokenizer = load_codellama_model(MODELS["CodeLlama"])
except Exception as e:
    logger.error(f"Error loading codellama model: {e}")
    raise HTTPException(status_code=500, detail = "Error loading Codellama model")

@router.post("/", name="codellama")
async def codellama_response(request: Request):
    data = await request.json()
    history = data["history"]
    user_input = data["user_input"]
    response = generate_codellama_response(history, user_input, model, tokenizer)
    return {"response": response}
