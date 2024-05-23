from flask import Blueprint, request, jsonify
from models.gpt import load_gpt_model, generate_gpt_response
from config import MODELS
import logging

router = Blueprint('gpt', __name__)
model, tokenizer = load_gpt_model(MODELS["GPT"])

@router.route('/', methods=['POST'])
def gpt_response():
    try:
        data = request.get_json()
        history = data.get("history", "")
        user_input = data.get("user_input", "")
        logging.info(f"Received request with history: {history}, user_input: {user_input}")
        response = generate_gpt_response(history, user_input, model, tokenizer)
        logging.info(f"Generated response: {response}")
        return jsonify({"response": response})
    except Exception as e:
        logging.error(f"Error in gpt_response: {e}")
        return jsonify({"error": "Something went wrong"}), 500
