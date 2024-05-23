from flask import Blueprint, request, jsonify
from models.gpt import load_gpt_model, generate_gpt_response
from config import MODELS
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

gpt_bp = Blueprint('gpt', __name__)

try:
    model, tokenizer = load_gpt_model(MODELS["GPT"])
    logger.info("GPT model and tokenizer loaded successfully.")
except Exception as e:
    logger.error(f"Error loading GPT model: {e}")
    model = None
    tokenizer = None

@gpt_bp.route('/', methods=['POST'])
def gpt_response():
    if model is None or tokenizer is None:
        return jsonify({"error": "Model not loaded"}), 500

    try:
        data = request.get_json()
        history = data.get("history")
        user_input = data.get("user_input")

        if not history or not user_input:
            raise ValueError("Missing 'history' or 'user_input' in request data")

        response = generate_gpt_response(history, user_input, model, tokenizer)
        logger.info(f"Generated response: {response}")
        return jsonify({"response": response})
    except ValueError as e:
        logger.error(f"ValueError: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return jsonify({"error": "Error generating response"}), 500
