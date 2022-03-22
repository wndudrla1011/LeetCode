nums = [2, 7, 11, 15]
target = 9

for i, n in enumerate(nums):
    complement = target - n

    # find complement in subset, find index of n and complement
    if complement in nums[i + 1:]:
        print([nums.index(n), nums[i + 1:].index(complement) + (i + 1)])
