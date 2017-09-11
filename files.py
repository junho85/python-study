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

mode = "rstrip"

if mode == "read":
    data = fh.read()
    print(data.upper().strip())
else:
    for line in fh:
        print(line.rstrip().upper())


fname = "mbox-short.txt"
fh = open(fname)
sum = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sum = sum + float(line[line.find(":")+1:])
    count = count + 1
print("Average spam confidence: ", sum/count)
