import inquirer
from dotenv import load_dotenv, dotenv_values
from src.scripts.issues.extract import extractIssues
from src.scripts.most_forks_repositories.extract import extractMostForks
from src.scripts.most_stars_repositories.extract import extractMostStars
from src.scripts.most_help_wanted_issues_repositories.extract import extractMostHelpWantedIssues
from src.scripts.main_repositories.extract import extractMain
from src.data_access.main_repositories import MainRepositories

load_dotenv()


token = dotenv_values()["GITHUB_TOKEN"]

print("\n----------------------------------------------------------------------------")
print("----------------------------- Github Extractor -----------------------------")
print("----------------------------------------------------------------------------\n")


questions = [
  inquirer.List('scripts',
                message="Extraction:",
                choices=['Extract - repositories', 'Extract - issues'],
            ),
]

answers = inquirer.prompt(questions)

if answers['scripts'] == 'Extract - repositories':

  print("\nExtracting: most forks repositories \n")
  extractMostForks(token)

  print("\nExtracting: most stars repositories \n")
  extractMostStars(token)

  print("\nExtracting: most help wanted issues repositories \n")
  extractMostHelpWantedIssues(token)

  print("\nExtracting: main repositories \n") 
  extractMain()

else:
  print("\n----------------------------------------------------------------------------\n")

  print("Date range:\n")
  print("** Date format:  YYYY-MM-DD")
  print("** Time format:  hh:mm:ss\n")

  startDate = input("Start date: ")

  startTime = input("Start time: ")

  endDate = input("End date: ")

  endTime = input("End time: ")

  print("\n----------------------------------------------------------------------------\n")

  print("Commits and PullRequests\n")

  questions = [
  inquirer.List('issueType',
                message="Would you like do extract:",
                choices=['Just issues', 'Just pull requests', 'Both'],
            ),
  ]

  answers = inquirer.prompt(questions)

  pr = True
  issue = True

  if(answers["issueType"] == 'Just issues'):
    pr = False
  if(answers["issueType"] == 'Just pull requests'):
    issue = False

  print("\n----------------------------------------------------------------------------\n")

  print("Logs \n")

  questions = [
  inquirer.List('logs',
                message="Enable logs?",
                choices=['Yes', 'No'],
            ),
  ]
  
  answers = inquirer.prompt(questions)
  
  log = True

  if(answers["logs"] == 'No'):
    log = False

  print("\n----------------------------------------------------------------------------\n")

  with MainRepositories() as main:
    repos = main.list()

  for repo in repos:
    print("\n----------------------------------------------------------------------------\n")
    print(f'Extracting issue with id: {repo[0]}')
    print("\n----------------------------------------------------------------------------\n")
    extractIssues(token, repo[1], repo[2], repo[0],f'{startDate}T{startTime}', f'{endDate}T{endTime}', issue, pr, log)
