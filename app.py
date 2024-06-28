from dotenv import load_dotenv
load_dotenv() # Loading all the environment variables from.env file

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to load the Gemini Pro Model to generate responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# Setup the Streamlit application
st.set_page_config(page_title="Gemini Chatbot", layout="wide")
st.header("Gemini LLM Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask a question!")


# When the submit button is clicked, generate the response
if submit:
    response = get_gemini_response(input)
    st.subheader("Generate Response is ")
    st.write(response)
