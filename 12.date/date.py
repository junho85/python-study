from datetime import date

today = date.today().strftime('%Y%m%d')

filename = today + ' ' + 'github.png'
print(filename)