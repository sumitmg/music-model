import streamlit as st

# Define all the notes
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Major scales
major_scales = {
    'C Major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'C# Major': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'],
    'D Major': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
    'D# Major': ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'],
    'E Major': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
    'F Major': ['F', 'G', 'A', 'A#', 'C', 'D', 'E'],
    'F# Major': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'],
    'G Major': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
    'G# Major': ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G'],
    'A Major': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
    'A# Major': ['A#', 'C', 'D', 'D#', 'F', 'G', 'A'],
    'B Major': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']
}

# Minor scales
minor_scales = {
    'C Minor': ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#'],
    'C# Minor': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
    'D Minor': ['D', 'E', 'F', 'G', 'A', 'A#', 'C'],
    'D# Minor': ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#'],
    'E Minor': ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
    'F Minor': ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#'],
    'F# Minor': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E'],
    'G Minor': ['G', 'A', 'A#', 'C', 'D', 'D#', 'F'],
    'G# Minor': ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#'],
    'A Minor': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'A# Minor': ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#'],
    'B Minor': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']
}

# Function to check if all selected notes are in the scale
def contains_all_notes(scale_notes, selected_notes):
    return all(note in scale_notes for note in selected_notes)

# Function to find possible scales for selected notes
def find_scales(selected_notes, major_scales, minor_scales):
    possible_scales = {
        'Major': [],
        'Minor': []
    }
    
    for scale, notes in major_scales.items():
        if contains_all_notes(notes, selected_notes):
            possible_scales['Major'].append(scale)
    
    for scale, notes in minor_scales.items():
        if contains_all_notes(notes, selected_notes):
            possible_scales['Minor'].append(scale)
    
    return possible_scales

# Streamlit app
st.title('Music Notes Helper Application')
st.write('Select 2 or more notes to find possible scales.')

# Multi-select for notes
selected_notes = st.multiselect('Select Notes', notes)

if len(selected_notes) >= 2:
    possible_scales = find_scales(selected_notes, major_scales, minor_scales)
    
    st.write('### Possible Major Scales:')
    for scale in possible_scales['Major']:
        st.write(scale)
    
    st.write('### Possible Minor Scales:')
    for scale in possible_scales['Minor']:
        st.write(scale)
else:
    st.write('Please select at least 2 notes.')
