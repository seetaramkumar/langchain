from transformers import AutoModel, AutoTokenizer

def load_codellama_model(model_name):
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

def generate_codellama_response(history, user_input, model, tokenizer):
    inputs = tokenizer(history + user_input, return_tensors="pt")
    outputs = model(**inputs)
    response = tokenizer.decode(outputs.logits.argmax(-1).squeeze(), skip_special_tokens=True)
    return response
