class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)

        # create a graph
        for u, v, w in times:
            graph[u].append((v, w))

        # declare Q
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            # have you never visited?
            if node not in dist:
                dist[node] = time
                # does the following path exist?
                for v, w in graph[node]:
                    # accumulate time(cost)
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # all are reachable from starting node
        if len(dist) == n:
            return max(dist.values())
            
        return -1