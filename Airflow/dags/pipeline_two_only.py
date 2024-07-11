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

def execute_pipeline_2():
    try:
        #Define o diretorio e o comando
        directory = r'C:\code-challenge-indicium-engdados\meltano'  # Usar 'r' antes da string para raw string literal
        command = 'meltano schedule run pipeline-2'

        # Executar o comando no prompt de comando do Windows
        subprocess.run(f'cd /d {directory} && {command}', shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

dag = DAG(
    'pipeline_two_only',
    default_args=default_args,
    description='Run only pipeline_2',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 7, 4),
    catchup=False,
)

task_part2 = PythonOperator(
    task_id='execute_pipeline_2',
    python_callable=execute_pipeline_2,
    dag=dag,
)
