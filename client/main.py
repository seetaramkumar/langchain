from client.interface import create_interface

MODELS = {
    "CodeLlama": "CodeLlama",
    "GPT": "GPT"
}

if __name__ == "__main__":
    create_interface(MODELS)
