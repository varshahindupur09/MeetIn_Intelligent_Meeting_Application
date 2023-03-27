import streamlit as st
import pandas as pd
import os

# Heading of the webpage
st.header('MeetIn')
st.subheader(' _- A Meeting Intelligence Application_')

st.write('\n')

# link to the audio files and read the audio files
dirname = os.getcwd()

meet_file_1= dirname + "/data/audio_1.mp3"
meet_file_2= dirname + "/data/audio_2.mp3"
meet_file_3= dirname + "/data/audio_3.mp3"
meet_file_4= dirname + "/data/audio_meet_v.mp3"

# show the meeting recordings 
option = st.selectbox(
    'Please select the meeting from below options?',
    (meet_file_1, meet_file_2, meet_file_3, meet_file_4))

st.write('You selected:', option)

st.audio(option, format='audio/mp3')

if 'but_b' not in st.session_state:
    st.session_state.disabled = True

print('before:', st.session_state)

button_a = st.button('transcribe_with_whisper', key='but_a')

button_b = st.button('generate_questions_with_chatgpt', key='but_b')


def transcribe_with_whisper(option):
    # callable function
    return "transcribed data with whisper"

if button_a:
    result = transcribe_with_whisper(option)
    st.write('Transcribed Text:')
    st.write(result)
    st.session_state.disabled = False

def generate_questions_with_chatgpt(option):
    # callable function
    return "Q: What was the meeting about?/n Q:How many participants are there in meeting?"

# generate questions 
if button_b:
    if not st.session_state.disabled:
        result_next = generate_questions_with_chatgpt(option)
        st.write('3-4 Questions on the above transcribed text: ')
        st.write(result_next)
    



