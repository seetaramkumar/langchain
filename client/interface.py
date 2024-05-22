import streamlit as st
import requests
from client.config import API_URL

def create_interface(models):
    st.title("Code Assistant Bot")
    st.write("Ask me anything about coding!")

    model_name = st.selectbox("Choose a model", list(models.keys()))

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    user_input = st.text_input("You: ", key="input")

    if st.button("Send"):
        if user_input:
            history = "\n".join([f"{turn['role'].capitalize()}: {turn['text']}" for turn in st.session_state.conversation])
            response = requests.post(
                f"{API_URL}/{model_name.lower()}",
                json={"history": history, "user_input": user_input}
            ).json()["response"]

            st.session_state.conversation.append({"role": "user", "text": user_input})
            st.session_state.conversation.append({"role": "bot", "text": response})

    for turn in st.session_state.conversation:
        if turn["role"] == "user":
            st.markdown(f"**You:** {turn['text']}")
        else:
            st.markdown(f"**Bot:** {turn['text']}")
