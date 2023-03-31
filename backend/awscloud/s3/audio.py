# %%
import os
import boto3
import boto3.s3
from dotenv import load_dotenv
from botocore.exceptions import ClientError
import time


# %%
load_dotenv()


# %%
aws_bucket_name = os.environ.get('S3_BUCKET_NAME')


# %%
s3_client = boto3.client("s3",
                    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                    aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'))

session = boto3.Session(
            region_name='us-east-1',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_KEY')
        )

s3 = session.resource('s3')
src_bucket = s3.Bucket(aws_bucket_name)

# %%
def upload_file_to_adhoc(file):

    try:   
        curr_time = round(time.time()*1000)
        file_name_only = file.filename.rsplit('.', 1)[0]
        file_extension = file.filename.rsplit('.', 1)[1]
        new_file_name = f"{file_name_only}-{curr_time}.{file_extension}"

        s3_client.upload_fileobj(file.file, Bucket= aws_bucket_name, Key = f"adhoc/{new_file_name}")

        return new_file_name

    except Exception as e:
        print(e)
        return None
    

def get_processed_audio_files() -> list:
    all_files = list()

    for object_summary in src_bucket.objects.filter(Prefix=  f'processed-audio/'):
        file_name = object_summary.key.split('/')[-1]
        if file_name != "":
            data = s3_client.get_object(Bucket = aws_bucket_name, Key = f"default-questions/{file_name.rsplit('.', 1)[0]}.txt")
            
            contents = data['Body'].read()
            
            all_files_with_default_question = dict()

            all_files_with_default_question["file_name"] = file_name
            all_files_with_default_question["default_question"] = contents.decode("utf-8")

            all_files.append(all_files_with_default_question)

    
    return all_files


def get_transcribed_audio_text(audio_file_name:str):
    
    data = s3_client.get_object(Bucket = aws_bucket_name, Key = f"processed-text/{audio_file_name.rsplit('.', 1)[0]}.txt")

    content = data['Body'].read()

    if len(content) == 0:
        return None
    else:
        return str(content,'utf-8')

