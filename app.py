# app.py
import streamlit as st

def app():
    st.set_page_config(
        page_title="Music Notes Helper",
        page_icon="🎵",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Welcome","Scale Visualization","Scale Finder"])

    if page == "Welcome":
        from Code import welcome
        welcome.show()
    elif page == "Scale Visualization":
        from Code import Homepage
        Homepage.homepage()
    elif page == "Scale Finder":
        from Code import scale_finder
        scale_finder.show()
