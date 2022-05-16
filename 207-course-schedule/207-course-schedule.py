class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)

        # create a graph
        for x, y in prerequisites:
            graph[x].append(y)

        # already visited node set
        traced = set()
        visited = set()


        def dfs(key):
            # if you come back to the node you visited: circular
            if key in traced:
                return False
            # pruning
            if key in visited:
                return True

            traced.add(key)
            # does the next course exist?
            for y in graph[key]:
                # not exist
                if not dfs(y):
                    return False

            # pruning
            traced.remove(key)
            visited.add(key)
            
            return True

        # search each node to the starting node
        for x in list(graph):
            if not dfs(x):
                return False
            
        return True