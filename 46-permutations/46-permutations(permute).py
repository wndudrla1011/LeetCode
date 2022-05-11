import itertools

nums = [1, 2, 3]

print(list(map(list, itertools.permutations(nums))))