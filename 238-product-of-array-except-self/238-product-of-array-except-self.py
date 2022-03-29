class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        left_list, right_list, result = [], [], []

        for num in nums:
            left_list.append(p)
            p = p * num

        p = 1
        for num in nums[::-1]:
            right_list.append(p)
            p = p * num

        right_list.reverse()

        for i in range(len(nums)):
            result.append(left_list[i] * right_list[i])

        return result