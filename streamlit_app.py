import streamlit as st

st.set_page_config(
    page_title="OnboardX",
    layout="wide"
)

st.title("📁 OnboardX")

uploaded_files = st.file_uploader(
    "Upload onboarding documents",
    accept_multiple_files=True,
    type=["pdf"]
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} files uploaded")
