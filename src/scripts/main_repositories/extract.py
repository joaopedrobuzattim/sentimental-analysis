from ...data_access.main_repositories import MainRepositories

def extractMain():
  with MainRepositories() as main:
    repos = main.listInterscetionRepositories()
  with MainRepositories() as main:
    for repo in repos:
      main.create(*repo)
  
    


  