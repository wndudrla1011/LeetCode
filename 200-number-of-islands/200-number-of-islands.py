class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(w, h):
        # if there's no more land, it's over
            if w < 0 or w >= len(grid) or h < 0 or h >= len(grid[0]) or grid[w][h] != '1':
                return

            # check visited point
            grid[w][h] = '0'

            # recursive search : north -> east -> south -> west
            dfs(w - 1, h)
            dfs(w, h + 1)
            dfs(w + 1, h)
            dfs(w, h - 1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # start searching from the current point
                    dfs(i, j)
                    # end a single search -> count + 1
                    count += 1

        return count