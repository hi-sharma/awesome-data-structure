from collections import defaultdict
class Solution:
    # O(n + e) time and space complexity. e = n*2
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # define dfs
        def dfs(node):
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
        # call dfs
        seen = set()
        ans = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                ans += 1
                dfs(i)
        return ans

        
