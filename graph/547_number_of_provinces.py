from collections import defaultdict
class Solution:
    # O(n*2) time O(n) space complexity
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # use dfs and adjacency list to store graph
        def dfs(node):
             neighbours = graph[node]
             for neighbour in neighbours:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)


        # create adjacency list
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()
        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        return ans
