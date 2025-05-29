from collections import defaultdict

# example5
print("## example5")
default_dict = defaultdict(dict, {
    "service": {"name": "my_service"}
})

print(default_dict)
print(default_dict["service"])
print(default_dict["service"]["name"])

# defaultdict
from collections import defaultdict

# example6
print("## example6")


default_dict = defaultdict(dict, {
    "service": {}
})

print(default_dict) # defaultdict(<class 'dict'>, {'service': {}})
print(default_dict["service"])  # {}
# Safe access using get method with a default value
print(default_dict["service"].get("name", "Key 'name' not found"))
# Or check before accessing
if "name" in default_dict["service"]:
    print(default_dict["service"]["name"])
else:
    print("Key 'name' not found in service dictionary")

