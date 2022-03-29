class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0

        for i, v2 in enumerate(nums):
            if i % 2 == 0:
                v1 = v2
            else:
                sum += min(v1, v2)
                
        return sum