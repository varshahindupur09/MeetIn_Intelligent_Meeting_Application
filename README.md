# Assignment4
Introducing MeetIn - a Meeting Intelligence Application. A voice-to-text pipeline was developed for this research can transcribe audio recordings and produce spoken transcripts. The GPT-3.5 Turbo model can also be used by the project to respond to user-posted default and custom questions.

# Links to the Live application

** Airflow: ** http://ec2-52-45-138-255.compute-1.amazonaws.com:8080/

** Streamlit: ** http://ec2-52-45-138-255.compute-1.amazonaws.com/

** FastAPI: ** http://ec2-52-45-138-255.compute-1.amazonaws.com:8000/docs

** Codelabs: ** https://docs.google.com/document/d/1KwFY_zq4X5mGg0K8itpnN3hzrCtn11xF6HUpXBjeMa0/edit?usp=sharing

# To execute this project, you will need:

1. Amazon Web Services account
2. Docker Desktop Application
3. AWS access and secret keys
4. OpenAI (Chat GPT) API key
5. Inside backend folder, create an .env file containing the following values
   .env
   AIRFLOW_UID=50000
   OPEN_AI_API_KEY=<openai_api_key>
   AWS_ACCESS_KEY=<aws_access_key>
   AWS_SECRET_KEY=<aws_secret_key>
   S3_BUCKET_NAME=<s3_bucket_name>
   
# Installation
1. Clone the repository (https://github.com/BigDataIA-Spring2023-Team-05/Assignment-04.git)
2. Create .env in 'Backend' (Streamlit & Fast API folder) and 'Airflow' which will contain the access keys to AWS S3 bucket and Airflow UID using the commands below: mkdir -p ./dags ./logs ./plugins echo -e "AIRFLOW_UID=$(id -u)" > .env
3. Postgres database is used to store GOES and NEXRAD data; MySQL database is used to store the details of Subscription Plans
4. Finally, create your own virtual environment by installing virtualenv package ('pip install virtualenv'), using 'py -m venv venv' to create a virtual environment of your own, next step is to download the packages in requirement.txt present in all directories by using 'pip install -r requirements.txt'

# The application usage instructions are as follows:

Access the Streamlit app by visiting the URL provided above.
Upload your meeting audio mp3 file by either dragging and dropping it onto the app or selecting it from your device.
Click on the 'Upload to s3' button.
Wait for a few minutes for the files to be processed, the duration of which will depend on the size of the mp3 file you uploaded.
Select the processed file you want from the dropdown list.
Choose to ask default questions or customize your own questions, and pose them to the application.
Once the questioning is complete, the application will provide you with answers to your questions.


# Architecture diagram
<img src="https://github.com/BigDataIA-Spring2023-Team-05/Assignment-04/blob/main/arch-diag.png">

# Team Information and Contribution

Name | Contribution 
--- | --- 
Rishabh Jain | 25% 
Venkata Sai Charan Amiti | 25% 
Varsha Hindupur | 25% 
Krishica Gopalakrishnan | 25% 

# ATTESTATION:

WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK.

   


