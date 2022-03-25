class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}

        for i, v in enumerate(nums):
            result[v] = i

        for i, v in enumerate(nums):
            if target - v in nums[i+1:]:
                return [i, result[target - v]]
                