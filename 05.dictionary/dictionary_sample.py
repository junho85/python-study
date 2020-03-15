some_dict = {'june': 12, 'hello': 22, 'world': 33}

print("=== keys ===")
for key in some_dict.keys():
    print(key, ":", some_dict[key])

print("=== keys auto - not recommend ===")
for key in some_dict:
    print(key, ":", some_dict[key])

print("=== items ===")
for key, value in some_dict.items():
    print(key, ":", value)
