class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums)):
            if nums[i] in result:
                return [result.index(nums[i]), i]
            result.append(target - nums[i])