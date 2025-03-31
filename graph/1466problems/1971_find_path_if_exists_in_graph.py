from collections import defaultdict
class Solution:
    # O(e) time and space complexity
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # perform dfs
        def dfs(node):
            if node == destination:
                return
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)

        # create adjacency list
        graph = defaultdict(list)
        for dx, dy in edges:
            graph[dx].append(dy)
            graph[dy].append(dx)
        
        # perform dfs from source
        seen = {source}
        dfs(source)
        return destination in seen
        
