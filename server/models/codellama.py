import logging
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_codellama_model(model_name):
    try:
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        return model, tokenizer
    except Exception as e:
        logging.error(f"Error loading CodeLlama model: {e}")
        raise

def generate_codellama_response(history, user_input, model, tokenizer):
    try:
        input_text = f"{history}\nUser: {user_input}\nBot:"
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=500)
        response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Process the response to extract relevant part
        response = response_text.split('Bot:')[-1].strip()
        return response
    except Exception as e:
        logging.error(f"Error generating response with CodeLlama: {e}")
        return "Sorry, something went wrong."
