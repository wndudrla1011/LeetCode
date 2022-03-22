nums = [2, 7, 11, 15]
target = 9

nums_map = {}

# key : num, value : index
for i, num in enumerate(nums):
    nums_map[num] = i

# whether 'target - num' exists and if it exists it get a different index compare num?
for i, num in enumerate(nums):
    if target - num in nums_map and i != nums_map[target - num]:
        print([i, nums_map[target - num]])
