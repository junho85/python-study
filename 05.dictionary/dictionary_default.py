# example1
my_dict = {
    "service": {"name": "my_service"}
}

print("example1")
print(my_dict.get("service").get("name"))  # my_service

# example2
my_dict = {
    "service": {}
}

print("example2")
print(my_dict.get("service").get("name"))  # None

# example3
my_dict = {}

print("example3")
# print(my_dict.get("service").get("name"))  # AttributeError: 'NoneType' object has no attribute 'get'

# example4
my_dict = {}

print("example4")
print(my_dict.get("service", {}).get("name"))  # None



# example5
my_dict = {
    "service": None
}

# print(my_dict.get("service", {}).get("name"))  # AttributeError: 'NoneType' object has no attribute 'get'

print((my_dict.get("service") or {}).get("name"))
