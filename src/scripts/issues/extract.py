import math
from ...data_access.issue import Issue
from ...data_access.comment import Comment
from ...data_access.reaction import Reaction
from ...utils import constants, functions
import datetime


def extractIssues(token, owner, repo, repositoryId, startDate, endDate, issue=True, pr=True, log=True):
    headers = {
        'Accept': constants.ACCEPT_HEADER,
        'Authorization': f'token {token}'
    }

    isArg = ''
    if not issue and pr:
        isArg = 'is:pr'
    if not pr and issue:
        isArg = 'is:issue'

    totalCount = functions.getUrl(f'{constants.BASE_URL}/search/issues',headers, params={
        'q': f'repo:{owner}/{repo} created:{startDate}..{endDate}'
    }).json()['total_count']
    
    totalPage = 0

    if totalCount >= 1000:
        totalPage = 10
    else:
        totalPage = math.ceil(totalCount / 100)
    
    if(log == True):
        print(f'\nThere are {totalCount} items remaining!\n')

    for page in range(1, totalPage + 1):
        issues = functions.getUrl(f'{constants.BASE_URL}/search/issues', headers, params = {
            'sort': 'created',
            'order': 'asc',
            'per_page': 100,
            'page': page,
            'q': f'repo:{owner}/{repo} {isArg} created:{startDate}..{endDate}'    
        }).json()

        if page == totalPage:
            lastElementDate = datetime.datetime.fromisoformat(issues['items'][len(issues['items']) - 1]['created_at'].replace("Z", ""))
            startDate = lastElementDate + datetime.timedelta(0,1)
            startDate = str(startDate).replace(' ', 'T')

        for item in issues['items']:
            if(log == True):
                print(f'Item number: {item["number"]}')
            with Issue() as i:
                createdIssueId = i.create(
                    repositoryId,
                    item["number"],
                    item["id"],
                    item["user"]["id"],
                    item["body"].replace("\x00", "\uFFFD") if item["body"] != None else item["body"],
                    "pull_request" if "pull_request" in item else "issue",
                    item["title"],
                    item["created_at"].replace('Z', ''),
                    item["updated_at"].replace('Z', ''),
                )
            with Reaction() as r:
                r.create(
                    createdIssueId,
                    None,
                    item["reactions"]["+1"],
                    item["reactions"]["-1"],
                    item["reactions"]["laugh"],
                    item["reactions"]["hooray"],
                    item["reactions"]["confused"],
                    item["reactions"]["heart"],
                    item["reactions"]["rocket"],
                    item["reactions"]["eyes"],
                )

            
            commentsUrl = f'{constants.BASE_URL}/repos/{owner}/{repo}/issues/{item["number"]}/comments'
            issueComments = functions.getUrl(commentsUrl, headers, params = {
                'sort': 'created',
                'order': 'asc'
            }).json()

            for comment in issueComments:
                if(log == True):
                    print(f'\tComment id: {comment["id"]}')
                if comment["user"]["type"] != 'Bot' and ( 
                    datetime.datetime.fromisoformat(comment['created_at'].replace('Z', '')) <= datetime.datetime.fromisoformat(endDate)  and
                    datetime.datetime.fromisoformat(comment['updated_at'].replace('Z', '')) <= datetime.datetime.fromisoformat(endDate)
                  ):
                    with Comment() as c:
                        createdCommentId = c.create(
                            comment["id"],
                            comment["user"]["id"],
                            createdIssueId,
                            comment["body"].replace("\x00", "\uFFFD"),
                            comment["created_at"].replace('Z', ''),
                            item["updated_at"].replace('Z', ''),
                        )
                    with Reaction() as r:
                        r.create(
                            None,
                            createdCommentId,
                            item["reactions"]["+1"],
                            item["reactions"]["-1"],
                            item["reactions"]["laugh"],
                            item["reactions"]["hooray"],
                            item["reactions"]["confused"],
                            item["reactions"]["heart"],
                            item["reactions"]["rocket"],
                            item["reactions"]["eyes"],
                        )

    if totalCount <= 1000:
        return
    extractIssues(token, owner, repo, repositoryId,startDate=startDate, endDate=endDate, issue=issue, pr=pr)
