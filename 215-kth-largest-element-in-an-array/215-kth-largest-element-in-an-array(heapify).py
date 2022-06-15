import heapq

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4


heapq.heapify(nums)

for _ in range(len(nums) - k):
    heapq.heappop(nums)

print(heapq.heappop(nums))
