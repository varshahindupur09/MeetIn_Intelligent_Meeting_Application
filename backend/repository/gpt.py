from awscloud.s3 import audio
from awscloud.cloudwatch.logger import audio_files_requested_by_user, question_asked_with_answer, file_uploaded_by_user
from util_openai.gpt import OpenAIUtil
from fastapi import status
from fastapi.responses import JSONResponse

def upload_audio_file_to_s3(file):
    is_uploaded = audio.upload_file_to_adhoc(file= file)

    if is_uploaded is True:
        file_uploaded_by_user(file_name= file.filename)
        return JSONResponse(
            content={
                'success': True, 
                'message': "File uploaded succesfully!"
            }
        )
    else:
        return JSONResponse(
            status_code= status.HTTP_400_BAD_REQUEST,
            content={
                'success': False, 
                'message': "File uploaded failed!"
            }
        )
    



def get_all_processed_audio_file():
    files = audio.get_processed_audio_files()


    if len(files) == 0:
        return JSONResponse(
            status_code= status.HTTP_204_NO_CONTENT,
            content={
                'success': False, 
                'message': "No files is processed yet"
            }
        )
    
    else:
        audio_files_requested_by_user(files= files)
        return JSONResponse(
            status_code= status.HTTP_200_OK,
            content={
                'success': True, 
                'message': "files available",
                'files_with_question': files
            }
        )

def get_answer_of_question_for_audio(audio_file: str, question: str):
    audio_transciption = audio.get_transcribed_audio_text(audio_file_name= audio_file)

    if audio_transciption is None:
        return JSONResponse(
            status_code= status.HTTP_404_NOT_FOUND,
            content={
                'success': False, 
                'message': "transcription not found",
            }
        )
    

    answer_response = OpenAIUtil().answer_questions_for_transcribed_text(transcription= audio_transciption, questions= question)


    if len(answer_response) == 0:
        question_asked_with_answer(audio_file_name= audio_file, question= question, answer= "Not able to generate answer")

        return JSONResponse(
            status_code= status.HTTP_200_OK,
            content={
                'success': False, 
                'message': "unable to generate answer",
            }
        )
    
    question_asked_with_answer(audio_file_name= audio_file, question= question, answer= answer_response)
    return JSONResponse(
            status_code= status.HTTP_200_OK,
            content={
                'success': True, 
                'audio_file_name': audio_file,
                'question_asked': question,
                'responded_answer': answer_response
            }
        )

    

        
    