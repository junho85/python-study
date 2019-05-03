from jira import JIRA

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

username = config['DEFAULT']['USERNAME']
password = config['DEFAULT']['PASSWORD']

print(username)

jira = JIRA('https://jira.atlassian.com')
# jira = JIRA('https://jira.atlassian.com', auth=(username, password))

issue = jira.issue('JRA-9')

print(issue.fields.project.key)             # 'JRA'
print(issue.fields.issuetype.name)          # 'New Feature'
print(issue.fields.reporter.displayName)    # 'Mike Cannon-Brookes [Atlassian]'