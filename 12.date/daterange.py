import calendar
from datetime import timedelta, date


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start = date(2019, 10, 1)

c = calendar.HTMLCalendar(calendar.SUNDAY)
first = next(c.itermonthdates(start.year, start.month))

for idx, date in enumerate(daterange(first, date.today())):
    print(date, end=' ')
    if idx % 7 == 6:
        print()
