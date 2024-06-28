from dotenv import load_dotenv
load_dotenv() # Loading all the environment variables from.env file

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Gemini Pro Model to generate responses
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
        return response.text
    else:
        response = model.generate_content(image)

    return response.text


# Setup the Streamlit application
st.set_page_config(page_title="Gemini Image Demo", layout="wide")
st.header("Gemini LLM Vision Application")

input = st.text_input("Input: ", key="input")


# Make a button to upload an image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg","jpeg"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Describe the Image to me!")

# When the submit button is clicked, generate the response
if submit:
    response = get_gemini_response(input, image)
    st.subheader("Generated Response is ")
    st.write(response)