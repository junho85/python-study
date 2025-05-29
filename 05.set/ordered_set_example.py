"""
https://pypi.org/project/ordered-set/
pip install ordered-set
"""
from ordered_set import OrderedSet

ordered_set = OrderedSet([3, 2, 1, 2, 3, 4])
print(ordered_set)  # OrderedSet([3, 2, 1, 4])

print("## get index by value")
print(ordered_set.get_loc(3)) # 0
print(type(ordered_set.get_loc(3))) # <class 'int'>
print(ordered_set.index(3))  # 0
print(type(ordered_set.index(3)))  # <class 'int'>

print(ordered_set.get_loc(1))  # 2
print(ordered_set.index(1))  # 2

print(ordered_set.get_loc(2))  # 1
print(ordered_set.index(2))  # 1

print(ordered_set.get_loc(4))  # 3
print(ordered_set.index(4))  # 3

print("## get item by index")
print(ordered_set[0])  # 3
print(ordered_set[1])  # 2
print(ordered_set[2])  # 1
print(ordered_set[3])  # 4