friends = [ 'Joseph', 'Glenn', 'Sally' ]
print(friends[2])
print(len(friends))

# fails with a traceback
# fruit = 'Banana'
# fruit[0] = 'b'
# print(fruit)

x = range(5)
for item in x:
    print(item)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))

t = [9, 41, 12, 3, 74, 15]
print(t[2:4])

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])