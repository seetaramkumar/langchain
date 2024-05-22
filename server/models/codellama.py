from transformers import AutoModelForCausalLM, AutoTokenizer

def load_codellama_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def generate_codellama_response(history, user_input, model, tokenizer):
    input_text = f"{history}\nUser: {user_input}\nBot:"
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=512)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("Bot:")[-1].strip()
