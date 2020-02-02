from jira import JIRA
import pprint

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

url = config['DEFAULT']['URL']
username = config['DEFAULT']['USERNAME']
password = config['DEFAULT']['PASSWORD']

if username:
    jira = JIRA(url, auth=(username, password))
else:
    jira = JIRA(url)


print("== In Progress ==")
for (idx, issue) in enumerate(jira.search_issues('assignee = june.kim and status = "In Progress"')):
    print(issue.key + "," + issue.fields.summary + "," + url + "/browse/" + issue.key)


print()
print("== Open ==")
for (idx, issue) in enumerate(jira.search_issues('assignee = june.kim and status = "Open"')):
    print(issue.key + "," + issue.fields.summary + "," + url + "/browse/" + issue.key)

print()
print("== find by WorkLogs ==")
# for issue in jira.search_issues('reporter = currentUser() order by created desc', maxResults=10):
issues = jira.search_issues(
    # 'worklogAuthor = currentUser() and worklogDate >= 2019-07-01 and worklogDate <= 2019-09-30 order by created desc',
    # 'worklogAuthor = currentUser() and worklogDate >= 2019-10-01 and worklogDate <= 2019-10-15 order by created desc',
    # 'worklogAuthor = currentUser() and worklogDate >= 2019-10-15 and worklogDate <= 2019-10-22 order by created desc',
    # 'worklogAuthor = currentUser() and worklogDate >= 2019-11-07',
    'worklogAuthor = june.kim and worklogDate >= 2019-12-24',
    maxResults=1000)

for (idx, issue) in enumerate(issues):
    # print(idx + 1)
    print(issue.key + "," + issue.fields.summary + "," + url + "/browse/" + issue.key)
    # print(issue.__dict__)
    # print(issue.fields.worklog)
    # print(issue.fields.worklog.worklogs)

    # for worklog in jira.worklogs(issue):
    #     # print(worklog)
    #     print(worklog.created, worklog.timeSpent, worklog.timeSpentSeconds)


for worklog in jira.worklogs("DAUMMAIL-842"):
    pprint.pprint(worklog)