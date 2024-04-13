import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageDraw, ImageFont

rawdata = pd.read_excel("Data/data.xlsx", sheet_name="Data")
rawdata['Frequency_cleaned'] = rawdata['Frequency'].apply(lambda x: float(x.strip()))
rawdata['note_type'] = rawdata['Notation'].apply(lambda x: "Black" if "/" in x else "White")
rawdata['Notation_cleaned'] = rawdata['Notation'].apply(lambda x: re.sub(r"/.*", "", x))
rawdata['key_alphabet'] = rawdata['Notation_cleaned'].apply(lambda x: x[0])
rawdata['note_number'] = rawdata['Notation_cleaned'].apply(lambda x: int(x[1]))
df = rawdata[['key_alphabet','Key number','note_number','note_type','Frequency_cleaned']]
hindi_notes=['सा','रे','ग','म','प','ध','नि']

# Open the image
img = Image.open('./Data/Image/realistic-88-piano-keys-illustration-free-vector.jpg')

key_number = df['Key number'].to_list()
note_type = df['note_type'].to_list()
draw_objects = {}
for i in key_number:
    draw_objects[i] = ImageDraw.Draw(img)

df_white = df.loc[df['note_type']=='White']
df_white_i = df_white.reset_index(drop=True)
df_white_i = df_white_i.reset_index().rename(columns={'index': 'colour_key_number'})
df_white_i

df_black = df.loc[df['note_type']=='Black']
df_black_i = df_black.reset_index(drop=True)
df_black_i = df_black_i.reset_index().rename(columns={'index': 'colour_key_number'})

df_final = pd.concat([df_white_i,df_black_i])
# Sort the concatenated DataFrame by the "key_number" column
sorted_df = df_final.sort_values(by='Key number')
# Reset the index
result_df = sorted_df.reset_index(drop=True)

def draw_placeholder(df,key_alphabet,note_type,scale):
    df_white = df.loc[df['note_type']=='White']
    df_black = df.loc[df['note_type']=='Black']
    df_white_key = df_white['colour_key_number'].to_list()
    df_black_key = df_black['Key number'].to_list()
    root_note = df[(df['key_alphabet']==key_alphabet) & (df['note_type']==note_type) & (df['note_number']==3)]['Key number'].iloc[0]
    
    # Open the image
    img = Image.open('./Data/Image/realistic-88-piano-keys-illustration-free-vector.jpg')
    x,k=0,0
    for i in df_white_key:
        note_number = df_white.loc[df_white['colour_key_number']==i]['note_number'].iloc[0]
        classical_note = df_white.loc[df_white['colour_key_number']==i]['classical_note'].iloc[0]
        draw_objects[i] = ImageDraw.Draw(img)
        x=30+i*35.85
        y = 350
        width, height = 30, 60
        # Draw a rectangle as a placeholder
        alpha=150
        fill_color = (255, 255, 0, alpha)
        if classical_note == 1:
            draw_objects[i].rectangle([x, y, x+width, y+height], fill='magenta')
        elif note_number==3:
            draw_objects[i].rectangle([x, y, x+width, y+height], fill=fill_color)
        else:
            draw_objects[i].rectangle([x, y, x+width, y+height], fill=fill_color)
    x,k=0,0
    for i in df_black_key:
        note_number = df_black.loc[df_black['Key number']==i]['note_number'].iloc[0]
        classical_note = df_black.loc[df_black['Key number']==i]['classical_note'].iloc[0]
        draw_objects[i] = ImageDraw.Draw(img)
        x=16+i*20.96
        y = 200
        width, height = 20, 60
        # Draw a rectangle as a placeholder
        if classical_note == 1:
            draw_objects[i].rectangle([x, y, x+width, y+height], width=2, fill='magenta')
        elif note_number==3:
            draw_objects[i].rectangle([x, y, x+width, y+height], width=2, fill=fill_color)
        else:
            draw_objects[i].rectangle([x, y, x+width, y+height], width=2, fill=fill_color)
    # Show the image
    # Create a drawing object
    draw_object_text = ImageDraw.Draw(img)
    draw_object_box = ImageDraw.Draw(img)

    # Define placeholder coordinates and size
    x, y = 500, 50
    width, height = 200, 50
    # Draw a rectangle as a placeholder
    draw_object_text.rectangle([x, y, x+width, y+height], outline='black', width=2, fill='yellow')

    font = ImageFont.truetype("./Data/Font/Akshar Unicode.ttf", 20)
    text1=""
    if note_type=="Black":
        text1="#"
    else:
        text1=""
    text = key_alphabet +" "+ text1+" "+scale
    text_width = draw_object_text.textlength(text, font=font)
    # Assuming your font size is stored in a variable called 'font_size'
    estimated_text_height = 2  # Assuming font size is available
    text_x = x + (width - text_width) / 2
    text_y = y + (height - estimated_text_height) / 2
    draw_object_text.text((text_x, text_y), text, fill='black', font=font)

    x, y = 600, 150
    width, height = 500, 300
    # Draw a rectangle as a placeholder
    draw_object_box.rectangle([x, y, x+width, y+height], outline='red', width=2)
    # Define font
    # Define the coordinates of the crop box (left, upper, right, lower)
    left = 345
    upper = 50
    right = 1360
    lower = 600
    # Crop the image
    cropped_image = img.crop((left, upper, right, lower))
    return cropped_image


def classical_notes(key_alphabet,note_type='White',scale='Major',key_number=4):
    major_sacle=[0,2,4,5,7,9,11,12]
    minor_sacle=[0,2,3,5,7,8,10,12]
    filtered_df = df[(df['key_alphabet'] == key_alphabet) & (df['note_type'] == note_type)]
    first_index = filtered_df.index[0]
    scale_index=[]
    max_value=0
    if scale=='Major':
        while max_value<88:
            for num in major_sacle:
                scale_index.append(first_index+num)
                max_value = max(scale_index)
            first_index = max_value
    if scale=='Minor':
        while max_value<88:
            for num in minor_sacle:
                scale_index.append(first_index+num)
                max_value = max(scale_index)
            first_index = max_value
    scale_index = [num for num in scale_index if num < 88]
    scale_index = list(set(scale_index))
    df_scale = result_df.loc[scale_index]
    df_small = df_scale.loc[(df_scale['note_number']>1) & (df_scale['note_number']<6)]
    df_small = df_small.reset_index(drop=True)
    # Define the starting number
    root_note = df_small[(df_small['key_alphabet']==key_alphabet) & (df_small['note_type']==note_type) & (df_small['note_number']==3)]['Key number'].iloc[0]
    starting_number = 8-df_small[df_small['Key number']==root_note].index[0]%7-1
    list_length = df_small.shape[0]
    repeat_range = 7
    # Create the list
    result_list = [(starting_number + i % repeat_range) % repeat_range + 1 for i in range(list_length)]
    df_small['classical_note']=result_list

    return df_small