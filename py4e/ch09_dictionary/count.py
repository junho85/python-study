name = "mbox-short.txt"
handle = open(name)

count = {}

for line in handle:
    if line.startswith("From "):
        key = line.split(" ")[1]
        count[key] = count.get(key, 0) + 1
        # if key in count:
        #     count[key] = count[key] + 1
        # else:
        #     count[key] = 1

max_value = None
max_key = None

for key, value in count.items():
    if max_value is None:
        max_value = value
        max_key = key
        next

    if value > max_value:
        max_value = value
        max_key = key

print(max_key, max_value)

