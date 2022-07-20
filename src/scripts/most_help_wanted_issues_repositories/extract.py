import requests
from ...data_access.most_help_wanted_issues_repositories import HelpWantedIssuesRepositories
from src.utils import constants


def extractMostHelpWantedIssues(token):
  
  headers = {
        'Accept': constants.ACCEPT_HEADER,
        'Authorization': f'token {token}'
}
  
  for i in range(1, 11):
    response = requests.get(f'{constants.BASE_URL}/search/repositories', headers=headers, params = {
      "sort": "help-wanted-issues",
      "per_page": 100,
      "page": i,
      "q": f'created:<=2019-01-01 stars:>=10000'
    }).json()

    print(f"{11 - i} pages remaining!\n")

    for item in response["items"]:
      with HelpWantedIssuesRepositories() as helpWantedIssuesRepositories:
        helpWantedIssuesRepositories.create(
          item["owner"]["login"],
          item["name"],
          item["id"],
          item["stargazers_count"],
          item["forks_count"],
          item['open_issues_count'],
          item["created_at"],
          item["updated_at"]
        )
