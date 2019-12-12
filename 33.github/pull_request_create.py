import yaml
from github import Github

with open('config.yaml') as file:
    configs = yaml.load(file, Loader=yaml.FullLoader)
    access_token = configs["access_token"]
    github_url = configs["github_url"]
    repo = configs["repo"]


g = Github(base_url=("%s/api/v3" % github_url), login_or_token=access_token)


repo = g.get_repo(repo)

title = 'v1.3.3'
body = 'some fix'
base = 'master'
head = 'develop'
repo.create_pull(title=title, body=body, base=base, head=head)
