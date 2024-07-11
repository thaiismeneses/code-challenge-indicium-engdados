from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

def execute_pipeline_1():
    try:
        command = 'cd /code-challenge-indicium-engdados/meltano && meltano schedule run pipeline-1'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stdout:
            print("Output:\n", stdout.decode())
        if stderr:
            print("Error:\n", stderr.decode())
    except Exception as e:
        print(f"An error occurred: {e}")

def execute_pipeline_2():
    try:
        command = 'cd /code-challenge-indicium-engdados/meltano && meltano schedule run pipeline-2'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stdout:
            print("Output:\n", stdout.decode())
        if stderr:
            print("Error:\n", stderr.decode())
    except Exception as e:
        print(f"An error occurred: {e}")

dag = DAG(
    'pipeline_one_and_two',
    default_args=default_args,
    description='Run pipeline_part1 followed by pipeline_2',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 7, 4),
    catchup=False,
)

task_part1 = PythonOperator(
    task_id='execute_pipeline_1',
    python_callable=execute_pipeline_1,
    dag=dag,
)

task_part2 = PythonOperator(
    task_id='execute_pipeline_2',
    python_callable=execute_pipeline_2,
    dag=dag,
)

task_part1 >> task_part2
