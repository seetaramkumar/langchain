import streamlit as st
from interface import get_bot_response

# Set the page configuration
st.set_page_config(page_title="Code Assistant Bot", layout="wide")

# Define a container for chat history
chat_container = st.container()

# Define a container for the user input at the bottom of the screen
input_container = st.container()

# Add the chat history to the chat container
with chat_container:
    if 'history' not in st.session_state:
        st.session_state.history = ""
    st.write(st.session_state.history)

# Model selection dropdown
with input_container:
    model_name = st.selectbox("Choose Model", ["CodeLlama", "GPT"], index=0)
    user_input = st.text_input("You:", key="user_input")

    # Send the user input and history to the model and get the response
    if st.button("Send"):
        if user_input:
            st.session_state.history += f"\nUser: {user_input}"
            try:
                bot_response = get_bot_response(model_name, st.session_state.history, user_input)
                st.session_state.history += f"\nBot: {bot_response}"
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error: {e}")

# Display the chat history again to reflect the updates
with chat_container:
    st.write(st.session_state.history)
