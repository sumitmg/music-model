# utils.py
from scales import major_scales, minor_scales

def contains_all_notes(scale_notes, selected_notes):
    return all(note in scale_notes for note in selected_notes)

def find_scales(selected_notes):
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
