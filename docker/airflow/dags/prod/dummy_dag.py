from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from utils.helpers import sleeper

now = datetime.now()

default_args = {
    'start_date': datetime(now.year, now.month, now.day),
}

with DAG('dummy_dag', default_args=default_args, schedule_interval='@daily') as dag:
    # DummyOperator represents a task with no actual functionality
    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task3 = DummyOperator(task_id='task3')

    sleeper_task1 = PythonOperator(
        task_id='sleeper_task1',
        python_callable=sleeper,
        op_kwargs={'sec': 10},
    )

    sleeper_task2 = PythonOperator(
        task_id='sleeper_task2',
        python_callable=sleeper,
        op_kwargs={'sec': 5},
    )

    task1 >> sleeper_task1 >> task2 >> sleeper_task2 >> task3
