from jira import JIRA

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

url = config['DEFAULT']['URL']
username = config['DEFAULT']['USERNAME']
password = config['DEFAULT']['PASSWORD']

jira = JIRA(url, auth=(username, password))

issue = jira.issue('QAKAKAOMAIL-175')
print(issue.fields.project.key)             # 'JRA'
print(issue.fields.issuetype.name)          # 'New Feature'
print(issue.fields.reporter.displayName)    # 'Mike Cannon-Brookes [Atlassian]'