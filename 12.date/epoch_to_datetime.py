import datetime

print(datetime.datetime.fromtimestamp(0))  # 1970-01-01 09:00:00


print(datetime.datetime(1970, 1, 1, 9, 0, 0).timestamp())  # 0.0

print(datetime.datetime.now())
