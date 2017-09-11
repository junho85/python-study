fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# fname = input('Enter the file name: ')
# fname = 'mbox-short.txt'
fname = 'mbox.txt'
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# fname = input("Enter file name: ")
fname = "mbox.txt"
fh = open(fname)
data = fh.read()
print(data.upper().strip())