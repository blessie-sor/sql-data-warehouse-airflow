from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.insert(0, '/opt/airflow')

from pipeline.runner import run_sql_file

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='medallion_pipeline',
    default_args=default_args,
    schedule='@daily',    
    catchup=False
) as dag:

    init_db = PythonOperator(
        task_id='init_database',
        python_callable=lambda: run_sql_file('/opt/airflow/scripts/init_database.sql')
    )

    bronze_ddl = PythonOperator(
        task_id='bronze_ddl',
        python_callable=lambda: run_sql_file('/opt/airflow/scripts/bronze/ddl_bronze.SQL')
    )

    load_bronze = PythonOperator(
        task_id='load_bronze',
        python_callable=lambda: run_sql_file('/opt/airflow/scripts/bronze/proc_load_bronze.SQL')
    )

    call_load_bronze = PythonOperator(
        task_id='call_load_bronze',
        python_callable=lambda: run_sql_file('/opt/airflow/scripts/bronze/proc_load_bronze.SQL')
    )

    silver_ddl = PythonOperator(
        task_id='silver_ddl',
        python_callable=lambda: run_sql_file('/opt/airflow/scripts/silver/ddl_silver.sql')
    )

    load_silver = PythonOperator(
        task_id='load_silver',
        python_callable=lambda: run_sql_file('/opt/airflow/scripts/silver/proc_load_silver.sql')
    )

    call_load_silver = PythonOperator(
        task_id='call_load_silver',
        python_callable=lambda: run_sql_file('/opt/airflow/scripts/silver/proc_load_silver.sql')
    )

    gold_ddl = PythonOperator(
        task_id='gold_ddl',
        python_callable=lambda: run_sql_file('/opt/airflow/scripts/gold/ddl_gold.sql')
    )

    # Define order
    init_db >> bronze_ddl >> load_bronze >> call_load_bronze >> silver_ddl >> load_silver >> call_load_silver >> gold_ddl