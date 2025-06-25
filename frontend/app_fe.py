import streamlit as st
import requests
import config
import os

st.title("Upload an Image File")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

APP_URL = os.getenv("APP_URL", "http://localhost:5000")


if uploaded_file is not None:
    # Prepare the file for POST request
    files = {
        'file': (uploaded_file.name, uploaded_file, uploaded_file.type)
    }
    # Send the file to the Flask backend
    response = requests.post(f'{APP_URL}/upload', files=files)
    if response.ok:
        st.write("Result from backend:")
        st.json(response.json())
    else:
        st.error(f"Error: {response.text}")