some_dict = {'june': [1,2,3], 'hello': [2,1,3], 'world': [33]}

# print(list(some_dict))
# keys = some_dict.keys()
# keys = list(some_dict)
# print(keys)

# names = set(some_dict.values())
# print(names)
#
# d = {}
# for n in names:
#     d[n] = [k for k in some_dict.keys() if some_dict[k] == n]

files = {
      'Input.txt': (1,2,3),
      'Code.py': (1,2,3),
      'Output.txt': (1,2)
   }

# files = {
#       'Input.txt': 'Randy',
#       'Code.py': 'Stan',
#       'Output.txt': 'Randy'
#    }


some_list = [u'chicken soup', u'chicken', u'cajun chicken salad']
print(some_list.sort())
print(sorted(some_list))

# d = {n:[k for k in files.keys() if files[k] == n] for n in set(files.values())}

names = set(files.values())

temp = {}
for n in names:
    temp[n] = [k for k in files.keys() if files[k] == n]



print("=== values ===")
print(temp.values())
# for value in temp.values():
#     print(value)
# print(result)

# for i in range(0, len(keys)):
#     for j in range(i+1, len(keys)):
#         print(keys[i], keys[j])

# for key in keys:
#     print(key)

# print(some_dict.values())
# print(some_dict.items())
#
# for key in some_dict.keys():
#     print(key, ":", some_dict[key])
#
# for key, value in some_dict.items():
#     print(key, ":", value)
