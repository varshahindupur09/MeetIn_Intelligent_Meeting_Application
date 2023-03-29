# %% 
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from datetime import timedelta
from pathlib import Path

import sys

sys.path.append('/opt/airflow/common_package/')


# import sys, os

# sys.path.append('/airflow/utils/')

# import aws_s3_bucket.AWSS3Download as AWSS3Download
# from audio_transcribe import AudioTranscribe

from openai_gpt import OpenAIGPT
from aws_s3_bucket import AWSS3Download
from audio_transcribe import AudioTranscribe


aws_cloud = AWSS3Download()
audio_transcribe = AudioTranscribe()
open_ai_gpt = OpenAIGPT()



# %%
dag = DAG(
    dag_id="adhoc",
    schedule="0 0 * * *",   # https://crontab.guru/
    start_date=days_ago(0),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=["labs", "damg7245"],
)


def test(**kwargs):
    print(2+3)



with dag:


    get_all_audio_files_from_s3 = PythonOperator(
        task_id='get_all_audio_files_from_s3',
        python_callable= aws_cloud.get_all_files,
        provide_context=True,
        do_xcom_push=True,
        dag=dag,
    )


    transcribe_audio = PythonOperator(
        task_id='transcribe_audio',
        python_callable= audio_transcribe.transcribe_audio_link,
        op_kwargs={"audio_file_url": "{{ ti.xcom_pull(task_ids='get_all_audio_files_from_s3') }}"},
        provide_context=True,
        do_xcom_push=True,
        dag=dag,
    )

    moving_transcription_to_aws_bucket = PythonOperator(
        task_id='moving_transcription_to_aws_bucket',
        python_callable= aws_cloud.store_transcript,
        op_kwargs={"audio_filename": "{{ ti.xcom_pull(task_ids='get_all_audio_files_from_s3') }}", "text" : "{{ ti.xcom_pull(task_ids='transcribe_audio') }}"},
        provide_context=True,
        dag=dag,
    )


    generate_deafult_questions_for_transcription = PythonOperator(
        task_id='generate_deafult_questions_for_transcription',
        python_callable= open_ai_gpt.generate_questions_for_transcribed_text,
        op_kwargs={"text" : ""},
        provide_context=True,
        dag=dag,
    )



    # Flow
    get_all_audio_files_from_s3 >> transcribe_audio >> moving_transcription_to_aws_bucket >> generate_deafult_questions_for_transcription
    # get_all_audio_files_from_s3 >> transcribe_audio