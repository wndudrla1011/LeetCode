nums = [6, 2, 6, 5, 1, 2]
sum = 0
nums.sort()

for i, n in enumerate(nums):
    if i % 2 == 0:
        sum += n

print(sum)
