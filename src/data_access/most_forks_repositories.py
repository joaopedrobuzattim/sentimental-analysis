from ..config import db


class ForksRepositories(db.Connection):
  def __init__(self):
    db.Connection.__init__(self)
  
  def create(self, *args):
    try:
      query = "INSERT INTO most_forks_repositories (owner, name ,repositoryId, stars, forks, openIssues, creationDate, updateDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
      result = self.query(query, args)
      return result[0][0]
    except Exception as e:
      print("Most forks repository insertion error: ", e)
      exit(1) 
