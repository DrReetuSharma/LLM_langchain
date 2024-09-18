import streamlit as st
from langchain.llms import OpenAI  # or chat_models.ChatOpenAI depending on your version

st.title("🔗 BioChemConversation App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    if openai_api_key.startswith("sk-"):
        model = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        response = model.predict(input_text)
        st.info(response)
    else:
        st.warning("Please enter a valid OpenAI API key!", icon="⚠")


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
