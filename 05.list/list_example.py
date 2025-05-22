list = ['d', 'a', 'c', 'b']

index = list.index('a')
print(index)  # 1
print(list[index + 1])  # c
print(list[index + 2])  # b
# print(list[index + 3])  # IndexError: list index out of range

print(list.pop(index + 1))  # c
print(list.pop(index + 1))  # b
# print(list.pop(index + 1))  # IndexError: pop index out of range
