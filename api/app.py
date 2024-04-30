from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
#from langchain_core.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn, os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv("chatbot/.env")

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)


#add_routes(app, Ollama(), path="/ollama")

llm = Ollama(model="codellama")

prompt = ChatPromptTemplate.from_template("{topic}")

add_routes(app, prompt|llm, path="/codeollama")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8091)

