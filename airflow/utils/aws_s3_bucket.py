# %%
from dotenv import load_dotenv
import os
import boto3
import boto3.s3


# %%
load_dotenv()

# %%
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')

# %%
class AWSS3Download:


    def __init__(self) -> None:
        

        self.processed_text_folder_name = 'processed-text/'

        session = boto3.Session(
            region_name='us-east-1',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_KEY')
        )
        s3 = session.resource('s3')
        self.src_bucket = s3.Bucket(S3_BUCKET_NAME)


    def get_all_files(self):
        files_available = list()

        for object_summary in self.src_bucket.objects.filter(Prefix=  f'adhoc/'):
            file_name = object_summary.key.split('/')[-1]
            files_available.append(file_name)

        return files_available

    def move_file_to_processes_folder(self, filename):
        copy_source = {
            'Bucket': S3_BUCKET_NAME,
            'Key': f'adhoc/{filename}'
        }

        try:
            self.src_bucket.copy(copy_source, f"adhoc-processed/{filename}")
            boto3.client('s3').delete_object(Bucket = S3_BUCKET_NAME, Key= "adhoc/" + filename)
            
            return True
        except Exception as e:
            print(e)
            return False

    def store_transcript(self, audio_filename:str, text: str):
        file_name = audio_filename.split(".")[0] + ".txt"

        file = open(file_name, 'w')
        file.write(text)
        file.close()

        self.src_bucket.upload_file(file_name, self.processed_text_folder_name + file_name)

        os.remove(file_name)


# %%
aws = AWSS3Download()

aws.move_file_to_processes_folder("podcast_2.mp3")

# %%
aws.get_all_files()
# https://damg-team-5-assignment-4.s3.amazonaws.com/adhoc/podcast_2.mp3

# %%
aws.store_transcript("podcast_2.mp3", "test tims")


# %%
