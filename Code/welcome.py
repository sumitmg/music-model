# pages/welcome.py
import streamlit as st

def show():
    st.title("Welcome to the Music Notes Helper App")
    st.write("""
        This app helps you find possible scales containing selected musical notes.
        
        Use the navigation menu on the left to go to the Scale Finder page and start selecting notes.
    """)
