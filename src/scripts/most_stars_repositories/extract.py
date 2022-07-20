import requests
from ...data_access.most_stars_repositories import StarsRepositories
from src.utils import constants


def extractMostStars(token):
  
  headers = {
        'Accept': constants.ACCEPT_HEADER,
        'Authorization': f'token {token}'
  }
  
  for i in range(1, 11):
    response = requests.get(f'{constants.BASE_URL}/search/repositories', headers=headers, params = {
      "sort": "stars",
      "order": "desc",
      "per_page": 100,
      "page": i,
      "q": f'created:<=2019-01-01 stars:>=10000'
    }).json()

    print(f"{10 - i} pages remaining!\n")

    for item in response["items"]:
      with StarsRepositories() as starsRepositories:
        starsRepositories.create(
          item["owner"]["login"],
          item["name"],
          item["id"],
          item["stargazers_count"],
          item["forks_count"],
          item['open_issues_count'],
          item["created_at"],
          item["updated_at"]
        )
