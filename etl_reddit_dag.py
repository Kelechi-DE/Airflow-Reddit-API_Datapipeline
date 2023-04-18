from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from datetime import datetime
from etl_reddit import reddit_extract_data


default_args = {
	'owner' : 'airflow', 
    'depends_on_past' : False,
	'start_date' : datetime(2023, 04, 20), 
	'email' : ['iamzamartech@gmail.com'], 	
	'email_on_failure' : False, 
	'email_on_retry' : False,  
	'retries' : 1,  
	'retry_delay' : timedelta(minutes = 1)
}									

dag = DAG(
	'ETL_DAG',  
	default_args = default_args,  
	description = 'ETL pipeline using RedditAPI'
	)
																
run_etl_task = PythonOperator(	
	task_id = 'reddit_ETL_pipeline', 
	dag = dag, 
	python_callable = reddit_extract_data
	)
						
run_etl_task