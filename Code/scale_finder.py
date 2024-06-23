# pages/scale_finder.py
import streamlit as st
from scales import notes
from utils import find_scales

def show():
    st.title('Scale Finder')
    st.write('Select 2 or more notes to find possible scales.')

    # Multi-select for notes
    selected_notes = st.multiselect('Select Notes', notes)

    if len(selected_notes) >= 2:
        possible_scales = find_scales(selected_notes)
        
        st.write('### Possible Major Scales:')
        for scale in possible_scales['Major']:
            st.write(scale)
        
        st.write('### Possible Minor Scales:')
        for scale in possible_scales['Minor']:
            st.write(scale)
    else:
        st.write('Please select at least 2 notes.')
