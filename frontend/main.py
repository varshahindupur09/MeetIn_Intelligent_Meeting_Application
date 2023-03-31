import streamlit as st

import os
import requests

BASE_URL=os.environ.get('FRONTEND_BASE_URL')

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.placeholder = ''
    st.session_state.select = True

# Heading of the webpage
st.write("# Welcome to MeetIn! 👋")
st.text("Ask questions from any audio file of your choice !")
# st.subheader(' This is a a Meeting Intelligence Application. We will be helping you with your audio transcribing and generate some questions based on the selected audio data.')
# Attach audio file
with st.form("my-form", clear_on_submit=True):
        audio_file = st.file_uploader("Choose an audio file", type=["mp3"])
        button_attribute = st.form_submit_button("Upload :arrow_up:")
    # st.subheader("Attach Audio File")
    

    # if audio_file:
    #     print(audio_file.name)
# Upload file to S3 bucket AWS

    # st.subheader("To AWS !")
if audio_file is not None:
    st.write("Selected Audio File :small_red_triangle_down:") 
    st.audio(audio_file, format='audio/mp3')
    st.session_state.select = True
else:
    st.warning("Please select Audio file")
    st.session_state.select = False


if button_attribute and st.session_state.select:
    # audio_file = st.session_state['audio_file']
    # st.session_state['audio_file'] = None
    print(audio_file.name)
    if st.session_state.select:
        # print("goin into loop")
        url = f'http://{BASE_URL}:8000/gpt/upload-audio'
        headers = {'accept': 'application/json'}
        files = {'file': (audio_file.name, audio_file.read(), 'audio/mpeg')}
        result = requests.post(url, headers= headers, files= files )
        
        output = result.json()
        print("-----------------------------")

        print(result.status_code)
        print(output)
        # print(output['success'])
        if result.status_code == 200 and audio_file is not None:
            st.success("Audio Uploaded!")
            st.session_state.select = True
        elif result.status_code == 400 and audio_file is not None:
            st.warning(output['message'])

st.write("\n")
st.write("\n")

## added the files via s3 bucket 
## code will be connected here

# link to the audio files and read the audio files
dirname = os.getcwd()



result_file_list = requests.get(f'http://{BASE_URL}:8000/gpt/processed-audio-files').json()

list_of_dict = result_file_list['files_with_question']
file_names = []
# Loop through the list of dictionaries
for item in list_of_dict:
# Access the value under the key 'file_names'
    file_name = item['file_name']
# Add the file_name to our list
    file_names.append(file_name)




# show the meeting recordings 
selected_audio_option = st.selectbox('Select the required file for Link',file_names)

st.write('You selected:', selected_audio_option)
st.write("\n")
st.write("\n")
if selected_audio_option:
    st.subheader("Generic Questions for above selected file")
    result_file_list = requests.get(f'http://{BASE_URL}:8000/gpt/processed-audio-files').json()
    list_of_dict = result_file_list['files_with_question']
    for item in list_of_dict:
        if item['file_name'] == selected_audio_option:
            st.write(str(item['default_question']))


# generic transcript questions
text_query = st.text_input(
        "Enter our question here 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )
st.write("\n")
st.write("\n")
# ask/upload question
button_ask_question = st.button('Ask Question', key='but_ask_questn')
if button_ask_question:
    payload = {'audio_file_name':str(selected_audio_option),'question':text_query}
    output = requests.get(f"http://{BASE_URL}:8000/gpt/question-transcript", params = payload).json()
    st.write(output["responded_answer"])

