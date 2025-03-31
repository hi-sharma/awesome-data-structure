from collections import defaultdict
class Solution:
    # O(n) time and space complexity
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # define dfs
        def dfs(node):
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in seen and neighbour not in restricted:
                    seen.add(neighbour)
                    dfs(neighbour)

        # convert for adjacency list
        graph = defaultdict(list)
        for dx, dy in edges:
            graph[dx].append(dy)
            graph[dy].append(dx)
        # perform dfs and stop if restricted nodes observed
        ans = 0
        seen = {0}
        restricted = set(restricted)
        dfs(0)
        return len(seen)


        
        
