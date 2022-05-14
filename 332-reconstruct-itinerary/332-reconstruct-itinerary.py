class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            # It is reachable?
            while graph[stack[-1]]:
                # searching next destination
                stack.append(graph[stack[-1]].pop(0))
            # Blocked destination
            route.append(stack.pop())

        return route[::-1]