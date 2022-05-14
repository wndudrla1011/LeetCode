class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []

        def dfs(a):
            # It is reachable?
            while graph[a]:
                # searching next destination
                dfs(graph[a].pop(0))
            # Blocked destination
            route.append(a)


        dfs('JFK')

        return route[::-1]