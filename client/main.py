import streamlit as st
import requests

# Function to send a POST request to the selected model's endpoint
def get_bot_response(model_name, history, user_input):
    api_url = f"http://localhost:8000/api/{model_name.lower()}"
    try:
        st.info(f"Sending request to {api_url}")
        response = requests.post(api_url, json={"history": history, "user_input": user_input})
        response.raise_for_status()
        data = response.json()
        st.info(f"Received response: {data}")
        if "response" in data:
            return data["response"]
        else:
            return data.get("error", "Sorry, something went wrong.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with the API: {e}")
        return "Sorry, something went wrong."

# Streamlit UI
st.title("Code Assistant Bot")

# User selects the model
model_name = st.selectbox("Select the model:", ["CodeLlama", "GPT"])

# Chat history
if "history" not in st.session_state:
    st.session_state.history = ""

# Display chat history
st.text_area("Conversation:", value=st.session_state.history, height=300, key="history_area")

# User input
user_input = st.text_input("You:", key="user_input")

# Handle user input
if st.button("Send"):
    if user_input:
        # Update history
        st.session_state.history += f"\nUser: {user_input}"
        bot_response = get_bot_response(model_name, st.session_state.history, user_input)
        st.session_state.history += f"\nBot: {bot_response}"
        st.experimental_rerun()
