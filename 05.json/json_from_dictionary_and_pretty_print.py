import json

print(json.dumps({'name': 'apple', 'address': 'usa'}))
# {"name": "apple", "address": "usa"}

# pretty printing - indent
print(json.dumps({'name': 'apple', 'address': 'usa'}, indent=2))
# {
#   "name": "apple",
#   "address": "usa"
# }

# sort_keys
print(json.dumps({'name': 'apple', 'address': 'usa'}, sort_keys=True, indent=2))
# {
#   "address": "usa",
#   "name": "apple"
# }

# separators
print(json.dumps({'name': 'apple', 'address': 'usa'}, indent=2, separators=('', '=')))
# {
#   "name"="apple"
#   "address"="usa"
# }

# ensure_ascii
print(json.dumps({'이름': 'apple', 'address': 'usa'}, indent=2, ensure_ascii=True))
# {
#   "\uc774\ub984": "apple",
#   "address": "usa"
# }

# allow_nan
print(json.dumps({'name': 'apple', 'NaN': float('nan'), 'infinity': float('inf')}, indent=2, allow_nan=True))
# {
#   "name": "apple",
#   "NaN": NaN,
#   "infinity": Infinity
# }

# print(json.dumps({'name': 'apple', 'NaN': float('nan'), 'infinity': float('inf')}, indent=2, allow_nan=False))
# ValueError: Out of range float values are not JSON compliant: nan
