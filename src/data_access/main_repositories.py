from ..config import db


class MainRepositories(db.Connection):
  def __init__(self):
    db.Connection.__init__(self)
  
  def listInterscetionRepositories(self,):
    try:
      query = 'select owner, name, repositoryId, stars, forks, openIssues, creationDate, updateDate from  \
            most_help_wanted_issues_repositories \
            intersect \
            select owner, name, repositoryId, stars, forks, openIssues, creationDate, updateDate from  \
            most_stars_repositories \
            intersect \
            select owner, name, repositoryId, stars, forks, openIssues, creationDate, updateDate from  \
            most_forks_repositories \
            order by openIssues desc \
            limit 100 \
            '
      result = self.query(query)
      return result
    except Exception as e:
      print("List Intersection error: ", e)
      exit(1) 
    

  def list(self):
    try:
      query = 'select * from main_repositories WHERE deletedAt IS NULL'
      result = self.query(query)
      return result
    except Exception as e:
      print("Main repository list error: ", e)
      exit(1) 

  def create(self, *args):
    try:
      query = "INSERT INTO main_repositories (owner, name ,repositoryId, stars, forks, openIssues, creationDate, updateDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
      result = self.query(query, args)
      return result[0][0]
    except Exception as e:
      print("Main repository insertion error: ", e)
      exit(1) 
