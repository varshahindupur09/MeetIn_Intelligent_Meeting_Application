from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from datetime import timedelta
from pathlib import Path

import sys
sys.path.append('/opt/airflow/common_package/')

from openai_gpt import OpenAIGPT
from aws_s3_bucket import AWSS3Download
from audio_transcribe import AudioTranscribe


aws_cloud = AWSS3Download()
audio_transcribe = AudioTranscribe()
open_ai_gpt = OpenAIGPT()



# %%
dag = DAG(
    dag_id="batch",
    schedule="0 1 * * *",   # https://crontab.guru/
    start_date=days_ago(0),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=["damg7245"],
)


with dag:


    get_all_audio_files_from_s3 = PythonOperator(
        task_id='get_all_batch_audio_files_from_s3',
        python_callable= aws_cloud.get_all_batch_files,
        provide_context=True,
        do_xcom_push=True,
        dag=dag,
    )


    transcribe_all_audio = PythonOperator(
        task_id='transcribe_all_batch_audio',
        python_callable= audio_transcribe.transcribe_batch_audio_link,
        op_kwargs={"audio_file_url": "{{ ti.xcom_pull(task_ids='get_all_audio_files_from_s3') }}"},
        provide_context=True,
        do_xcom_push=True,
        dag=dag,
    )

    get_all_audio_files_from_s3 >> transcribe_all_audio