# %%
import os
import time
import boto3
from dotenv import load_dotenv

# %%
load_dotenv()

# %%

log_group_name = os.environ.get('AWS_LOG_GROUP_NAME')

clientlogs = boto3.client(
                        'logs', 
                        region_name='us-east-1',
                        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                        aws_secret_access_key=os.environ.get('AWS_SECRET_KEY')
                        )
# %%
def question_asked_with_answer(audio_file_name: str, question:str, answer:str):
    clientlogs.put_log_events(
        logGroupName = log_group_name,
        logStreamName = os.environ.get('AWS_CLOUD_WATCH_NAME_QUESTION_ANSWER'),
        logEvents=[
            {
                'timestamp':int(time.time()*1e3),
                'message': f"Audio file used:\n{audio_file_name}\n\nUser asked question:\n{question}\n\nModel Responded with following answer:\n{answer}"
            }
        ]
    )


def audio_files_requested_by_user(files:list):
    clientlogs.put_log_events(
        logGroupName = log_group_name,
        logStreamName = os.environ.get('AWS_CLOUD_WATCH_NAME_FILES_REQUESTED'),
        logEvents=[
            {
                'timestamp':int(time.time()*1e3),
                'message': f"Files requested by the user:\n{files}"
            }
        ]
    )



def file_uploaded_by_user(file_name:str):
    clientlogs.put_log_events(
        logGroupName = log_group_name,
        logStreamName = os.environ.get('AWS_CLOUD_WATCH_NAME_FILE_UPLOADED'),
        logEvents=[
            {
                'timestamp':int(time.time()*1e3),
                'message': f"Files uploaded by the user:\n{file_name}"
            }
        ]
    )
