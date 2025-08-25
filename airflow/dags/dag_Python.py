from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator

def my_python_function():
    print('Hello!!!')

with DAG(
    'dag_python', 
    start_date=days_ago(1),
    schedule_interval='@daily'
) as dag:
    
    run_python_task = PythonOperator(
        task_id='Python_start',
        python_callable=my_python_function
        # op_kwargs={'name': 'Alice', 'age': 30}
    )