from collections import defaultdict
class Solution:
    # O(n) time and space iterative solution
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x,y))

        seen = {0}
        ans = 0
        stack = [0]
        while stack:
            node = stack.pop()
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in seen:
                    if (node, neighbour) in roads:
                        ans += 1
                    seen.add(neighbour)
                    stack.append(neighbour)
        return ans


        
