### del statement
mydict = {"name": "hong gil dong", "age": 28}

print(mydict) # {'name': 'hong gil dong', 'age': 28}

del mydict["name"]

print(mydict) # {'age': 28}

# del mydict["name"] # KeyError: 'name'

if 'name' in mydict:
    del mydict["name"]

### pop

print(mydict.pop("name", None)) # None

# mydict.pop("name") # KeyError: 'name'