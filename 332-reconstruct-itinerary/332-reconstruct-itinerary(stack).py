import collections

tickets = [["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"], ["JFK", "AXA"], ["ANU", "JFK"], ["ADL", "ANU"],
           ["TIA", "AUA"], ["ANU", "AUA"], ["ADL", "EZE"], ["ADL", "EZE"], ["EZE", "ADL"], ["AXA", "EZE"],
           ["AUA", "AXA"], ["JFK", "AXA"], ["AXA", "AUA"], ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"],
           ["EZE", "ANU"], ["AUA", "ANU"]]

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

print(route[::-1])