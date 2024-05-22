from fastapi import APIRouter, Request
from server.models.codellama import load_codellama_model, generate_codellama_response
from server.config import MODELS

router = APIRouter()
model, tokenizer = load_codellama_model(MODELS["CodeLlama"])

@router.post("/codellama")
async def codellama_response(request: Request):
    data = await request.json()
    history = data["history"]
    user_input = data["user_input"]
    response = generate_codellama_response(history, user_input, model, tokenizer)
    return {"response": response}
