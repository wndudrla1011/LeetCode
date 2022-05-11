class Solution(object):
    def letterCombinations(self, D):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(index, path):
            if len(path) == len(D):
                result.append(path)
                return

            for i in range(index, len(D)):
                for j in pad[D[i]]:
                    dfs(i + 1, path + j)


        if not D:
            return []
            
        pad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        dfs(0, "")
        
        return result