class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def dfs(index, path):
            result.append(path[:])

            if index == len(nums):
                return

            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()


        dfs(0, [])
        
        return result