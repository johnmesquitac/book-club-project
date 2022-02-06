import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta, datetime

default_args = {
   'owner': 'jsanto29',
   'depends_on_past': False,
   'start_date': datetime(2019, 1, 1),
   'retries': 0,
   }

with DAG(
   'first-dag',
   schedule_interval=timedelta(minutes=10),
   catchup=False,
   default_args=default_args
) as dag:
   t1 = BashOperator(
      task_id='first_etl',
      bash_command="""
         "C:\Users\mesqu\Documents\Scrapping-Books-Project\venv\Scripts\python.exe"
          "C:\Users\mesqu\Documents\Scrapping-Books-Project\retrieving_data_from_page\books_data.py"
      """)
   t2 = BashOperator(
      task_id='second_etl',
      bash_command="""
         "C:\Users\mesqu\Documents\Scrapping-Books-Project\venv\Scripts\python.exe"
         "C:\Users\mesqu\Documents\Scrapping-Books-Project\inserting_into_db\inserting_data_db.py"
      """)

t1 >> t2
