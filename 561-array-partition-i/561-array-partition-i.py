class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pair, n = 2, 0
        sum = 0
        nums.sort()

        while pair * n != len(nums):
            sum += min(nums[pair * n], nums[pair * n + 1])
            n += 1

        return sum