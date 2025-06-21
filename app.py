import streamlit as st
from doc_parsing import extract_and_upload

st.title("Upload an Image File")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    result = extract_and_upload(uploaded_file)
    st.write(result)