import yaml

with open('members.yaml') as file:
    members = yaml.load(file, Loader=yaml.FullLoader)
    print(members)
