# Introducing MeetIn - a Meeting Intelligence Application
A voice-to-text pipeline was developed for this research can transcribe audio recordings and produce spoken transcripts. The GPT-3.5 Turbo model can also be used by the project to respond to user-posted default and custom questions.

## Links to the Live application 

** Airflow: ** http://ec2-52-45-138-255.compute-1.amazonaws.com:8080/

** Streamlit: ** http://ec2-52-45-138-255.compute-1.amazonaws.com/

** FastAPI: ** http://ec2-52-45-138-255.compute-1.amazonaws.com:8000/docs

## To execute this project, you will need:

1. Amazon Web Services account
2. Docker Desktop Application
3. AWS access and secret keys
4. OpenAI (Chat GPT) API key
5. Create an .env file in the main directory containing the following information
   .env
   AIRFLOW_UID=50000
   AIRFLOW_PROJ_DIR=./airflow
   OPEN_AI_API_KEY=
   AWS_ACCESS_KEY=
   AWS_SECRET_KEY=
   S3_BUCKET_NAME=damg-team-5-assignment-4
   AWS_LOG_GROUP_NAME=damg-assignment-4
   AWS_CLOUD_WATCH_NAME_QUESTION_ANSWER=question-asked-with-answer
   AWS_CLOUD_WATCH_NAME_FILES_REQUESTED=files-requested-by-user
   AWS_CLOUD_WATCH_NAME_FILE_UPLOADED=file-uploaded-by-user
   AIRFLOW_USERNAME=airflow
   AIRFLOW_PASSWORD=airflow
   FRONTEND_BASE_URL=backend
   AIRFLOW_BASE_URL=airflow-webserver
   
## sample.env (refer to this)
<img src="https://github.com/BigDataIA-Spring2023-Team-05/Assignment-04/blob/main/env%20sample.jpeg">

   
## Installation
1. Clone the repository (https://github.com/BigDataIA-Spring2023-Team-05/Assignment-04.git)
2. Create .env in 'Backend' (Streamlit & Fast API folder) and 'Airflow' which will contain the access keys to AWS S3 bucket and Airflow UID using the commands below: mkdir -p ./dags ./logs ./plugins echo -e "AIRFLOW_UID=$(id -u)" > .env
3. Postgres database is used to store GOES and NEXRAD data; MySQL database is used to store the details of Subscription Plans
4. Finally, create your own virtual environment by installing virtualenv package ('pip install virtualenv'), using 'py -m venv venv' to create a virtual environment of your own, next step is to download the packages in requirement.txt present in all directories by using 'pip install -r requirements.txt'

## The application usage instructions are as follows:

Access the Streamlit app by visiting the URL provided above.
Upload your meeting audio mp3 file by either dragging and dropping it onto the app or selecting it from your device.
Click on the 'Upload to s3' button.
Wait for a few minutes for the files to be processed, the duration of which will depend on the size of the mp3 file you uploaded.
Select the processed file you want from the dropdown list.
Choose to ask default questions or customize your own questions, and pose them to the application.
Once the questioning is complete, the application will provide you with answers to your questions.


## Architecture diagram
Here is the Architecture Diagram of our projects, the major tools we have used in this assignment are

Streamlit UI
Airflow
Chat GPT
MySQL Database

<img src="https://github.com/BigDataIA-Spring2023-Team-05/Assignment-04/blob/main/ArchDiag.png">

## Website Page
<img src="https://github.com/varshahindupur09/MeetIn_Intelligent_Meeting_Application/blob/main/meetin_firstpage.png"></img>

AIM
The major aim of this application is to derive necessary information from the audio files and answer the required questions entered by the user with the help of FAST API

OUR APPLICATION UTILIZES FOLLOWING LIBRARIES:

Streamlit
Chatgpt API
Airflow
AWS cloudwatch
AIRFLOW

RECORDING DESCRIPTION:

We have recorded 4 audio files consisting of various informations regarding latest technology, multilingual conversations, normal conversations , songs and podcast informations

The airflow of our project majorly has two DAG's running:

## ADHOC PROCESS:

The Adhoc DAG consists of four major Tasks to run in the airflow pipeline

The first functionality that we do is to read the audio from adhoc folder in the S3 bucket.
The audio file that is available in the adhoc folder is sent through the whisper API.
With the help of Whisper API transcription services we reliably and quickly transcribe audio and video content of our call into a text file successfully,this transcript is now written into S3's processed folder.
Once this is done we store the transcribed texts into a separate categorized adhoc folder in the S3 bucket
Now we invoke the chatgpt API with the help of REST API,where a call is made from the information we have at hand and we ask the questions related to our transcribed text.
Along with this we input some initial default questions into the Database

<img src="https://github.com/varshahindupur09/MeetIn_Meeting_Intelligence_Application/blob/main/meetin_airflow_adhoc_dag.png"></img>

## BATCH DAG PROCESS:

Similar to the Adhoc process,we have the batch DAG process which runs four tasks in the airflow

The first functionality that we do is to read the audio from adhoc folder in the S3 bucket.
The audio file that is available in the adhoc folder is sent through the whisper API.
With the help of Whisper API transcription services we reliably and quickly transcribe audio and video content of our call into a text file successfully,this transcript is now written into S3's processed folder.
Once this is done we store the transcribed texts into a separate categorized batch folder in the S3 bucket.
Now we invoke the chatgpt API which gets initiated with the help if cron to ask the questions related to our transcribed text.
Along with this we input some initial default questions into the database.

<img src="https://github.com/varshahindupur09/MeetIn_Meeting_Intelligence_Application/blob/main/meetin_airflow_batch_dag.png"></img>

## DEPLOYMENT ON CLOUD
Our application is deployed in the aws cloud and it is hosted

Hosting our website in amazon S3 bucket is an option as we want any of the user's audio's in order to dynamically generate questions related to the audio's posted by the user's.

## CHATGPT API
We invoke the Chat API whenever we want our function's to generate the questions related to our audio files by making necessary HTTP requests to the API endpoints with the given API key and pass in the required parameters according to the input available in our streamlit UI.

The Chatgpt API does the following things in our application:

Once the API is invoked it acts on the question entered by the user according to the audio selected.
Some generic questions regarding the audio are generated once we invoke the gpt API based on the files uploaded in the S3 folder.


## Project Directory Structure
```
📦 Assignment-04
├─ .DS_Store
├─ .github
│  └─ workflows
│     └─ main.yml
├─ .gitignore
├─ README.md
├─ airflow
│  ├─ .gitignore
│  ├─ Dockerfile
│  ├─ __init__.py
│  ├─ common_package
│  │  ├─ __init__.py
│  │  ├─ audio_transcrib
│  │  ├─ aws_s3_bucket.py
│  │  └─ openai_gpt.py
│  └─ dags
│     ├─ __pycache__
│     │  └─ adhoc.cpython-37.pyc
│     ├─ adhoc_dag.py
│     └─ batch_dag.py
├─ arch-diag.png
├─ backend
│  ├─ Dockerfile
│  ├─ awscloud
│  │  ├─ __init__.py
│  │  ├─ cloudwatch
│  │  │  ├─ __init__.py
│  │  │  └─ logger.py
│  │  └─ s3
│  │     ├─ __init__.py
│  │     └─ audio.py
│  ├─ main.py
│  ├─ repository
│  │  ├─ __init__.py
│  │  └─ gpt.py
│  ├─ requirements.txt
│  ├─ routers
│  │  ├─ __init__.py
│  │  └─ gpt.py
│  ├─ setup.py
│  ├─ team5.egg-info
│  │  ├─ PKG-INFO
│  │  ├─ SOURCES.txt
│  │  ├─ dependency_links.txt
│  │  └─ top_level.txt
│  ├─ util_openai
│  │  ├─ __init__.py
│  │  └─ gpt.py
│  └─ utils
│     ├─ __init__.py
│     ├─ airflow_dag.py
│     └─ logger.py
├─ docker-compose.yml
├─ env sample.jpeg
├─ frontend
│  ├─ Dockerfile
│  ├─ main.py
│  └─ requirements.txt
├─ nginx
│  ├─ Dockerfile
│  └─ project.conf
└─ sample.env
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)
