#%%
import whisper
import boto3
import os
import boto3
import boto3.s3
import botocore
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

#%%
# dirname = os.getcwd()
# print(dirname)

#%%
load_dotenv()

S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')

#%%
session = boto3.Session(
    region_name='us-east-1',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.environ.get('AWS_ACCESS_KEY_SECRET')
)

# s3 = session.resource('s3')

s3 = session.client('s3')

# print(source_file)

source_file= "/Users/varshahindupur/Documents/GitHub/Model_as_a_service/data/audio.mp3"

s3.upload_file(
    Filename=source_file,
    Bucket=S3_BUCKET_NAME,
    Key="unprocessed_audio_file_1",
)

# audio_file_url='https://damg-team-5-assignment-4.s3.amazonaws.com/Everyday+I+want+to+Fly.mp3' (already there)

audio_source_link = f'https://damg-team-5-assignment-4.s3.amazonaws.com/{source_file}'

model = whisper.load_model("base")
result = model.transcribe(audio_source_link)

print(result["text"])

result_file = 'audio_1_song_processed.txt'

with open(result_file, 'w') as f:
    f.write(result["text"])

s3.upload_file(
    filename=result_file,
    Bucket=os.environ.get('S3_BUCKET_NAME'),
    Key="audio_1_song_processed",
)

s3.download_file(
    Bucket=os.environ.get('S3_BUCKET_NAME'), Key="audio_1_song_processed", Filename=result_file
)

# # %%

# %%
