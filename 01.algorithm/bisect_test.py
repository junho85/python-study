import bisect

apply_order = [9, 10, 6, 5, 4, 3, 1]
sorted_apply_order = sorted(set(apply_order))
print(sorted_apply_order) # [1, 3, 4, 5, 6, 9, 10]

print(bisect.bisect_left(sorted_apply_order, 3)) # 1
print(bisect.bisect_right(sorted_apply_order, 3)) # 2
print(bisect.bisect(sorted_apply_order, 3)) # 2
