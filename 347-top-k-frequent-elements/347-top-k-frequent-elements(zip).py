import collections

nums = [4, 1, -1, 2, -1, 2, 3]
k = 2

print(list(zip(*collections.Counter(nums).most_common(k)))[0])