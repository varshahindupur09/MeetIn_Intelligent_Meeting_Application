from fastapi import APIRouter, status, File, UploadFile
from fastapi.responses import JSONResponse
from typing import Union
from utils.logger import Log
from repository.gpt import upload_audio_file_to_s3, get_all_processed_audio_file, get_answer_of_question_for_audio

router = APIRouter(
    prefix='/gpt',
    tags=['GPT']
)


@router.post('/upload-audio', status_code= status.HTTP_201_CREATED)
async def create_upload_file(file: Union[UploadFile, None] = None):
    if not file:
        return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    'success': False, 
                    "message":  "No upload file sent",
                }
            )
    else:
        if str("audio") not in str(file.content_type):
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    'success': False, 
                    "message":  "Please upload a valid audio file",
                }
            )

        Log().i(str(file.filename))
        return upload_audio_file_to_s3(file= file)


@router.get('/processed-audio-files', status_code= status.HTTP_200_OK)
async def get_all_processed_audio_files():
    return get_all_processed_audio_file()


@router.get('/question-transcript', status_code= status.HTTP_200_OK)
async def question_transcript(audio_file_name: str, question: str):
    return get_answer_of_question_for_audio(audio_file= audio_file_name, question= question)