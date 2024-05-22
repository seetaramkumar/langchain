from fastapi import APIRouter, Request, HTTPException
from models.codellama import load_codellama_model, generate_codellama_response
from config import MODELS
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
try:
    model, tokenizer = load_codellama_model(MODELS["CodeLlama"])
    logger.info("Codellama model and tokenizer loaded successfully.")
except Exception as e:
    logger.error(f"Error loading Codellama model: {e}")
    raise HTTPException(status_code=500, detail="Error loading Codellama model")

@router.post("")
async def codellama_response(request: Request):
    try:
        data = await request.json()
        history = data.get("history")
        user_input = data.get("user_input")

        if history is None or user_input is None:
            raise ValueError("Missing 'history' or 'user_input' in request data")

        response = generate_codellama_response(history, user_input, model, tokenizer)
        logger.info(f"Generated response: {response}")
        return {"response": response}
    except ValueError as e:
        logger.error(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail="Error generating response")
