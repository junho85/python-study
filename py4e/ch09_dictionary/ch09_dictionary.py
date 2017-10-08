# part 1
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
# {'age': 21, 'course': 182}

ddd['age'] = 23
print(ddd)
# {'age': 23, 'course': 182}

lst = list()
lst.append(21)
lst.append(183)
print(lst)
# [21, 183]

jjj = {'chuck': 1, 'fred': 42}
print(jjj)

# part 2
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen'] + 1
print(ccc)


counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


# part 3 Dictionaries and Files

some_dict = {'june': 12, 'hello': 22, 'world': 33}
print(list(some_dict))
print(some_dict.keys())
print(some_dict.values())
print(some_dict.items())

for key in some_dict.keys():
    print(key, ":", some_dict[key])

for key, value in some_dict.items():
    print(key, ":", value)

# Traceback
# stuff = dict()
# print(stuff['candy']) # KeyError: 'candy'

stuff = dict()
print(stuff.get('candy', -1))
