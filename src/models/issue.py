from unittest import result
from ..config import db


class Issue(db.Connection):
  def __init__(self):
    db.Connection.__init__(self)
  
  def create(self, *args):
    try:
      query = "INSERT INTO issues (issueNumber, issueId, userId, body, type, title, creationDate, updateDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
      result = self.query(query, args)
      return result[0]
    except Exception as e:
      print("Insertion error: ", e)
      exit(1) 

