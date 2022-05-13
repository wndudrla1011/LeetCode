class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []


        def dfs(elem, v):
            if sum(elem) == target:
                result.append(elem[:])
                return
            elif sum(elem) > target:
                return


            for i in range(v, len(candidates)):
                if candidates[i] == 0:
                    return
                elem.append(candidates[i])
                dfs(elem, i)
                elem.pop()


        dfs([], 0)
        
        return result