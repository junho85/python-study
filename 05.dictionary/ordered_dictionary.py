"""
https://docs.python.org/3/library/collections.html#collections.OrderedDict
"""
from collections import OrderedDict

mylist = [
    "list1",
    "list2",
    "list3",
    "list4",
    "list5",
    "list6",
    "list7",
    "list8",
    "list9",
    "list10",
]

ordered_dict = OrderedDict.fromkeys(mylist, 0)
print(ordered_dict)
print(ordered_dict.get("list100"))

key_list = list(ordered_dict.keys())
index = key_list.index('list8')
print(index)