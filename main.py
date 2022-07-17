import scripts.issues.extract as issues
from dotenv import load_dotenv, dotenv_values

load_dotenv()


token = dotenv_values()["GITHUB_TOKEN"]

print("\n----------------------------------------------------------------------------")
print("----------------------------- Github Extractor -----------------------------")
print("----------------------------------------------------------------------------\n")


print("Repository name and owner: \n")


org = input("Organization: ")
repo = input("Repository: ")

print("\n----------------------------------------------------------------------------\n")

print("Date range:\n")
print("** Date format:  YYYY-MM-DD")
print("** Time format:  hh-mm-ss\n")


startDate = input("Start date: ")

startTime = input("Start time: ")

endDate = input("End date: ")

endTime = input("End time: ")

print("\n----------------------------------------------------------------------------\n")

print("Commits and PullRequests\n")

issueType = int(input("Would you like do extract:  Just issues (1) | just pull requests (2) | both (3)   "))

pr = True
issue = True

if(issueType == 1):
  pr = False
if(issueType == 2):
  issue = False

print("\n----------------------------------------------------------------------------\n")

print("Logs \n")

logInput = input("Enable logs? y / n:   ")

log = True

if(log == 'n' or log == 'N'):
  log = False

print("\n----------------------------------------------------------------------------\n")

issues.extract(token, org, repo, f'{startDate}T{startTime}', f'{endDate}T{endTime}', issue, pr, log)
