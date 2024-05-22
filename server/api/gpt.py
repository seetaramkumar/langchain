from fastapi import APIRouter, Request
from server.models.gpt import load_gpt_model, generate_gpt_response
from server.config import MODELS

router = APIRouter()
model, tokenizer = load_gpt_model(MODELS["GPT"])

@router.post("/gpt")
async def gpt_response(request: Request):
    data = await request.json()
    history = data["history"]
    user_input = data["user_input"]
    response = generate_gpt_response(history, user_input, model, tokenizer)
    return {"response": response}
