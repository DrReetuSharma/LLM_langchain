import streamlit as st
from langchain.llms import OpenAI  # Ensure you have the correct import

st.title("🔗 BioChemConversation App")

# Sidebar for OpenAI API Key
openai_api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")


def generate_response(input_text):
    # Ensure the API key starts with 'sk-' before proceeding
    if openai_api_key.startswith("sk-"):
        # Initialize the model with the provided API key
        model = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        response = model.predict(input_text)
        st.info(response)
    else:
        st.warning("Please enter a valid OpenAI API key!", icon="⚠")


# Create the form inside the main section of the app
with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What is Lipinski's rule?",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        if openai_api_key.startswith("sk-"):
            generate_response(text)
        else:
            st.warning("Please enter your OpenAI API key!", icon="⚠")
