from flask import Blueprint, request, jsonify
from models.codellama import load_codellama_model, generate_codellama_response
from config import MODELS
import logging

router = Blueprint('codellama', __name__)
model, tokenizer = load_codellama_model(MODELS["CodeLlama"])

@router.route('/', methods=['POST'])
def codellama_response():
    try:
        data = request.get_json()
        history = data.get("history", "")
        user_input = data.get("user_input", "")
        logging.info(f"Received request with history: {history}, user_input: {user_input}")
        response = generate_codellama_response(history, user_input, model, tokenizer)
        logging.info(f"Generated response: {response}")
        return jsonify({"response": response})
    except Exception as e:
        logging.error(f"Error in codellama_response: {e}")
        return jsonify({"error": "Something went wrong"}), 500
