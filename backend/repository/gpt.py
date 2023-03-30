from awscloud.s3 import audio
from fastapi import status
from fastapi.responses import JSONResponse

def upload_audio_file_to_s3(file):
    is_uploaded = audio.upload_file_to_adhoc(file= file)

    if is_uploaded is True:
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
        return JSONResponse(
            status_code= status.HTTP_200_OK,
            content={
                'success': False, 
                'message': "files available",
                'files': files
            }
        )
        