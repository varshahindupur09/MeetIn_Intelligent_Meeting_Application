# %% 
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from datetime import timedelta
from utils.aws_s3_bucket import AWSS3Download
from utils.audio_transcribe import AudioTranscribe
from utils.openai_gpt import OpenAIGPT


aws_cloud = AWSS3Download()
audio_transcribe = AudioTranscribe()
open_ai_gpt = OpenAIGPT()


# %%
dag = DAG(
    dag_id="sandbox",
    schedule="0 0 * * *",   # https://crontab.guru/
    start_date=days_ago(0),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=["labs", "damg7245"],
)



with dag:


    get_all_audio_files_from_s3 = PythonOperator(
        task_id='Get audio file to transcribe',
        python_callable= aws_cloud.get_all_files(),
        dag=dag,
    )


    transcribe_audio = PythonOperator(
        task_id='Transcribing audio file',
        python_callable= audio_transcribe.transcribe_audio_link(""),
        provide_context=True,
        dag=dag,
    )

    moving_transcription_to_aws_bucket = PythonOperator(
        task_id='Moving transcribed text to AWS S3 Bucket',
        python_callable= aws_cloud.store_transcript(audio_filename= "", text= ""),
        provide_context=True,
        dag=dag,
    )


    generate_deafult_questions_for_transcription = PythonOperator(
        task_id='Generate questions for the transcription',
        python_callable= open_ai_gpt.generate_questions_for_transcribed_text(text= ""),
        provide_context=True,
        dag=dag,
    )



    # Flow
    get_all_audio_files_from_s3 >> transcribe_audio >> moving_transcription_to_aws_bucket >> generate_deafult_questions_for_transcription