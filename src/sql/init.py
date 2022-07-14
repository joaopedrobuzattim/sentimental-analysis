
import psycopg2
from dotenv import load_dotenv, dotenv_values
import sys
import os

load_dotenv()


database = dotenv_values()["PG_DATABASE"]
host = dotenv_values()["PG_HOST"]
password = dotenv_values()["PG_PASSWORD"]
username = dotenv_values()["PG_USERNAME"]
port = dotenv_values()["PG_PORT"]

try:
  conn = psycopg2.connect(
    user=username, 
    password=password, 
    host=host,
    port=port
  )

  conn.autocommit = True

  cur1 = conn.cursor()
  
  cur1.execute(f'CREATE DATABASE {database}')

  
  conn.close()


except Exception as e:
  print("Database creation error: ", e)


try:
  conn = psycopg2.connect(
    user=username, 
    password=password, 
    host=host,
    port=port,
    database=database
  )

  conn.autocommit = True

  cur = conn.cursor()

  cur.execute(open(os.path.join(sys.path[0],'issues.sql'), 'r').read())
  cur.execute(open(os.path.join(sys.path[0],'comments.sql'), 'r').read())
  cur.execute(open(os.path.join(sys.path[0],'reactions.sql'), 'r').read())
  
  conn.close()


except Exception as e:
  print("Table creation error: ", e)