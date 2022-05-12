class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []


        def dfs(elem, start, k):
            if k == 0:
                result.append(elem[:])
                return

            for i in range(start, n + 1):
                elem.append(i)
                dfs(elem, i + 1, k - 1)
                elem.pop()


        dfs([], 1, k)
        
        return result