import configparser

from jira import JIRA

config = configparser.ConfigParser()
config.read('config.ini')

url = config['DEFAULT']['URL']
username = config['DEFAULT']['USERNAME']
password = config['DEFAULT']['PASSWORD']

if username:
    jira = JIRA(url, auth=(username, password))
else:
    jira = JIRA(url)

print()
print("== Resolved ==")
project = 'MYPROJECT'  # Replace with your actual project key
for (idx, issue) in enumerate(jira.search_issues('project = %s and status = "Resolved"' % project)):
    print(issue.key + "," + issue.fields.summary + "," + url + "/browse/" + issue.key)

