import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.google.cloud.operators.dataflow import DataflowCreatePythonJobOperator

# Fecha de inicio del DAG (ayer)
yesterday = datetime.combine(datetime.today() - timedelta(1), datetime.min.time())

# Argumentos por defecto del DAG
default_args = {
    'start_date': yesterday,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=30)
}

# Definición del DAG
with DAG(
    dag_id='DataflowPythonOperator_TwoSteps',
    catchup=False,
    schedule_interval=timedelta(days=1),
    default_args=default_args
) as dag:

    # Tarea de inicio
    start = DummyOperator(task_id='start')

    # Primera tarea: proceso de logs (Job 1)
    dataflow_batch_process_logs_1 = DataflowCreatePythonJobOperator(
        task_id='dataflow_batch_process_logs_1',
        py_file='gs://us-central1-composerdevelop-b648feb4-bucket/dags/scripts/composer_dataflow.py',
        options={
            'output': 'gs://beam_dataflow_cl/results'
        },
        dataflow_default_options={
            'project': 'sesion04-461702',
            'staging_location': 'gs://beam_dataflow_cl/staging',
            'temp_location': 'gs://beam_dataflow_cl/temp',
            'zone': 'us-central1-c'
        }
    )

    # Segunda tarea: proceso adicional (Job 2)
    dataflow_batch_process_logs_2 = DataflowCreatePythonJobOperator(
        task_id='dataflow_batch_process_logs_2',
        py_file='gs://us-central1-composerdevelop-b648feb4-bucket/dags/scripts/composer_dataflow1.py',
        options={
            'output': 'gs://beam_dataflow_cl/results'
        },
        dataflow_default_options={
            'project': 'sesion04-461702',
            'staging_location': 'gs://beam_dataflow_cl/staging',
            'temp_location': 'gs://beam_dataflow_cl/temp',
            'zone': 'us-central1-c'
        }
    )

    # Tarea final
    end = DummyOperator(task_id='end')

    # Definición del flujo
    start >> dataflow_batch_process_logs_1 >> dataflow_batch_process_logs_2 >> end
















