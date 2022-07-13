import typing
from ..config import db


class Comment(db.Connection):
  def __init__(self):
    db.Connection.__init__(self)
  
  def create(self, *args):
    try:
      query = "INSERT INTO comments (commentId, userId ,issueId, body, creationDate, updateDate) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
      result = self.query(query, args)
      return result[0]
    except Exception as e:
      print("Insertion error: ", e)
      exit(1) 

