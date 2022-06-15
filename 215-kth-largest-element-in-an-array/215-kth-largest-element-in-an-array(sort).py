import heapq

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

# nums.sort()
# print(nums[-k])

print(sorted(nums, reverse=True)[k-1])