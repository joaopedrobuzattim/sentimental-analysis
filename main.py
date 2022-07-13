import src.scripts.extractor as extractor
from dotenv import load_dotenv, dotenv_values
from pprintpp import pprint

load_dotenv()


token = dotenv_values()["GITHUB_TOKEN"]


print("----------------------------- Github Extractor -----------------------------")
print("\n")

print("Repository name and owner: \n")


org = input("Organization: ")
repo = input("Repository: ")

print("\nDate range:")
print("** Date format:  2020-04-02T19:43:43\n")


startDate = input("Start date: ")
endDate = input("End date: ")

print("\n Commits/PullRequests\n")

issueType = int(input("Would you like do extract:  Just issues (1) | just pull requests (2) | both (3)"))

pr = True
issue = True

if(issueType == 1):
  pr = False
if(issueType == 2):
  issue = False

extractor.extract(token, org, repo, startDate, endDate, issue, pr)
