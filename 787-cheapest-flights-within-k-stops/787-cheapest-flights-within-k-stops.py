class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)

        # create a graph
        for s, d, c in flights:
            graph[s].append((d, c))

        visited = {}

        # Q = [(cost, source)]
        Q = [(0, src, 0)]

        # via = transferred count
        while Q:
            cost, node, via = heapq.heappop(Q)
            # arrived dst
            if node == dst:
                return cost
            # pruning (don't go to visited node)
            if node not in visited or visited[node] > via:
                visited[node] = via
                # transfer k+1 times from src
                for d, c in graph[node]:
                    if via <= k:
                        alt = cost + c
                        heapq.heappush(Q, (alt, d, via + 1))

        return -1