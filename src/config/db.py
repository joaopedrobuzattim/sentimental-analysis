from dotenv import load_dotenv, dotenv_values
import psycopg2 as pg


load_dotenv()

config = {
  "user": dotenv_values()['PG_USERNAME'],
  "password": dotenv_values()['PG_PASSWORD'],
  "host": dotenv_values()["PG_HOST"],
  "port" : dotenv_values()["PG_PORT"],
  "database": dotenv_values()["PG_DATABASE"]
}

class Connection():
  def __init__(self):
    self.config = config
    self.connection = None
    self.cursor = None

  def __enter__(self):
    try:
      self.connection = pg.connect(**self.config) 
      self.cursor = self.connection.cursor()
    except Exception as e:
      print("Connection error: ", e)
      exit(1) 
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_tb is None:
        self.connection.commit()
    else:
        self.connection.rollback()
    self.connection.close()

  def fetchAll(self):
    return self.cursor.fetchall()
  
  def fetchOne(self):
    return self.cursor.fetchone()

  def commit(self):
    return self.connection.commit()
  
  def query(self, sql, params=()):
    self.cursor.execute(sql, params)
    return self.fetchOne()
