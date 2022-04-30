import collections
import heapq

nums = [4, 1, -1, 2, -1, 2, 3]
k = 2

freqs = collections.Counter(nums)
freqs_heap = []

for f in freqs:
    heapq.heappush(freqs_heap, (-freqs[f], f))

topk = []
for _ in range(k):
    topk.append(heapq.heappop(freqs_heap)[1])

print(topk)