import streamlit as st
import Modules.code as cd

st.title("My Music Application")

st.title('Music Scale Visualizer')

# Define input widgets for key_alphabet, note_type, and scale
key_alphabet = st.selectbox('Enter Key Alphabet', ['C', 'D','E', 'F','G', 'A','B'])
note_type = st.selectbox('Select Note Type', ['Black', 'White'])
scale = st.selectbox('Select Scale', ['Major', 'Minor'])

# Add a button to trigger the draw_placeholder function
if st.button('Generate Scale'):
    # Call the draw_placeholder function with the provided inputs
    df_scale= cd.classical_notes(key_alphabet=key_alphabet,note_type=note_type,scale=scale,key_number=4)
    cd.draw_placeholder(df_scale, key_alphabet=key_alphabet, note_type=note_type, scale=scale)
