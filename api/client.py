import requests
import streamlit as st


def get_codellama_response(input_text):
    response = requests.post("http://localhost:8080/codellama/invoke",
                             json = {'input':{'topic':input_text}})
    
    return response.json()['output']


st.title("CodeAI using LangChain")
input_text = st.text_input("Ask me anything on ML and Python")


if input_text:
    st.write(get_codellama_response(input_text))