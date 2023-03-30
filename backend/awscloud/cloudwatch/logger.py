# %%
import os
import time
import boto3
from dotenv import load_dotenv

# %%
load_dotenv()

# %%

log_group_name=os.environ.get('AWS_LOG_GROUP_NAME')

clientlogs = boto3.client(
                        'logs', 
                        region_name='us-east-1',
                        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                        aws_secret_access_key=os.environ.get('AWS_ACCESS_KEY_SECRET')
                        )
# %%
def write_goes_log(message:str):
    clientlogs.put_log_events(
        logGroupName = log_group_name,
        logStreamName = "goes-logs",
        logEvents=[
            {
                'timestamp':int(time.time()*1e3),
                'message':message
            }
        ]
    )
