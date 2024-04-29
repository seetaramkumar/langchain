from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("LANGCHAIN_API_KEY"))

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    ("system", "Act as an Python and ML developer and help to respond to user queries with proper examples"),
    ("user", "Question: {question}")
)

st.title("LangChain Demo...")
input_text = st.text_input("Ask me anything on Python or ML")

llm = Ollama(model="codellama")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
