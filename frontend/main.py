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

def transcribe_with_whisper(option):
    # callable function
    return "transcribed data with whisper"

if st.button('transcribe_with_whisper'):
    result = transcribe_with_whisper(option)
    st.write('Transcribed Text:')
    st.write(result)

def generate_questions_with_chatgpt(option):
    # callable function
    return "Q: What was the meeting about?/n Q:How many participants are there in meeting?"

# generate questions 
if st.button('generate_questions_with_chatgpt'):
    result_next = generate_questions_with_chatgpt(option)
    st.write('3-4 Questions on the above transcribed text: ')
    st.write(result_next)



