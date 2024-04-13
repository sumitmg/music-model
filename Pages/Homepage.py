import streamlit as st
import Modules.code as cd


def homepage():
    st.title('Music Scale Visualizer')
    col1, col2, col3= st.columns(3)
    # Define input widgets for key_alphabet, note_type, and scale
    with col1:
        key_alphabet = st.selectbox('Enter Key Alphabet', ['C', 'D', 'E', 'F', 'G', 'A', 'B'], format_func=lambda x: x)
    with col2:
        note_type = st.radio('Select Note Type', ['Black', 'White'])
    with col3:    
        scale = st.radio('Select Scale', ['Major', 'Minor'])

    # Call the draw_placeholder function with the provided inputs
    df_scale= cd.classical_notes(key_alphabet=key_alphabet,note_type=note_type,scale=scale,key_number=4)
    img = cd.draw_placeholder(df_scale, key_alphabet=key_alphabet, note_type=note_type, scale=scale)
    st.image(img, caption='Realistic Piano Keys', use_column_width=True)
