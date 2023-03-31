import requests
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()

airflow_username = os.environ.get('AIRFLOW_USERNAME')
airflow_password = os.environ.get('AIRFLOW_PASSWORD')
airflow_base = os.environ.get('AIRFLOW_BASE_URL')


def trigger_airflow_adhoc_dag(file_name: str):
    try:
        now = datetime.utcnow()
        date_string = now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

        url = f'http://{airflow_base}:8080/api/v1/dags/adhoc/dagRuns'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        data = {
            "conf": {
                "audio_file_url": f"https://damg-team-5-assignment-4.s3.amazonaws.com/adhoc/{file_name}"
            },
            "dag_run_id": f"FASTAPI-RUN-{date_string}",
            "logical_date": date_string,
            "note": f"FASTAPI-RUN-{date_string}\n\nFile executed: {file_name}"
        }

        response = requests.post(url, headers=headers, json=data, auth=(str(airflow_username), str(airflow_password)))
        print(response)

        return True
    finally:
        return True
