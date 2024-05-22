from fastapi import APIRouter, Request, HTTPException
from models.gpt import load_gpt_model, generate_gpt_response
from config import MODELS
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
try:
    model, tokenizer = load_gpt_model(MODELS["GPT"])
    logger.info("GPT model and tokenizer loaded successfully.")
except Exception as e:
    logger.error(f"Error loading GPT model: {e}")
    raise HTTPException(status_code=500, detail="Error loading GPT model")

@router.post("/")
async def gpt_response(request: Request):
    try:
        data = await request.json()
        history = data.get("history")
        user_input = data.get("user_input")

        if not history or not user_input:
            raise ValueError("Missing 'history' or 'user_input' in request data")

        response = generate_gpt_response(history, user_input, model, tokenizer)
        logger.info(f"Generated response: {response}")
        return {"response": response}
    except ValueError as e:
        logger.error(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail="Error generating response")
