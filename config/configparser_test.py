import configparser

config = configparser.ConfigParser()
config.read('config.ini')

username = config['DEFAULT']['USERNAME']
password = config['DEFAULT']['PASSWORD']

print(username)
print(password)