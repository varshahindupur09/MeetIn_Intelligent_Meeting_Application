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
def upload_file_to_adhoc(file) -> bool:

    try:   
        curr_time = round(time.time()*1000)
        file_name_only = file.filename.rsplit('.', 1)[0]

        s3_client.upload_fileobj(file.file, Bucket= aws_bucket_name, Key = f"adhoc/{file_name_only}-{curr_time}.mp3")

        return True

    except Exception as e:
        print(e)
        return False
    

def get_processed_audio_files() -> list:
    all_files = list()

    for object_summary in src_bucket.objects.filter(Prefix=  f'processed-audio/'):
        file_name = object_summary.key.split('/')[-1]
        if file_name != "":
            all_files.append(file_name)

    
    return all_files
