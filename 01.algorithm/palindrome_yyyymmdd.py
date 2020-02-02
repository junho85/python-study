import math
from datetime import timedelta, date


def is_palindrome(input_str):
    half = len(input_str) / 2
    left = input_str[:int(half)]
    right = input_str[math.ceil(half):][::-1]

    if left == right:
        return True
    else:
        return False


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start = date(2020, 1, 1)
end = date(2999, 12, 31) + timedelta(1)

for idx, date in enumerate(daterange(start, end)):
    date_yyyymmdd = date.strftime("%Y%m%d")
    if is_palindrome(date_yyyymmdd):
        print(date_yyyymmdd)
