class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 1:
            return [0]

        # create bidirectional graph
        graph = collections.defaultdict(list)
        for i, j, in edges:
            graph[i].append(j)
            graph[j].append(i)

        # add the first leaf nodes
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # repeat removing leaf nodes by there are no more than two left node
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves