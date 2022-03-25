class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        p = 1
        # left multiple
        for i in range(len(nums)):
            result.append(p)
            p *= nums[i]

        p = 1
        # right multiple
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * p
            p = p * nums[i]

        return result