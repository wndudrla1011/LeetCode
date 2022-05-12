class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        arr = [0 for i in range(n+1)]

        result = []

        def dfs(v, visited = []):
            if collections.Counter(arr)[1] == k:
                result.append(visited[:])
                return

            for i in range(v, n+1):
                if i not in visited:
                    visited.append(i)
                    arr[i] = 1
                dfs(i+1, visited)
                visited.pop()
                arr[i] = 0

        dfs(1, [])
        
        return result