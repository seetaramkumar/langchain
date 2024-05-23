import requests
from config import API_URL

def get_bot_response(model_name, history, user_input):
    response = requests.post(f"{API_URL}/{model_name.lower()}", json={"history": history, "user_input": user_input})
    print("reponse: ", response)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()["response"]
