import streamlit as st


def user_login():
    username = st.sidebar.text_input("Username", value="Todd", max_chars=20)
    username = username.replace(",", "")
    st.sidebar.header(f"Hi {username}!")
    return username
