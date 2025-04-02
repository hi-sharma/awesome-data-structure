'''
1. Prepare a directed graph
2. Get all nodes with in-degree=0, put them in the queue
3. Process queue and remove edges visited
4. Repeat from step-2
5. If no nodes with 0 indegree found and graph is not null -> return empty array
'''
from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        # Prepare the graph - adjacency list
        graph = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1

        queue = deque([i for i in range(numCourses) if i not in indegree])
        while queue:
            vertex = queue.popleft()
            ans.append(vertex)
            neighbours = graph.get(vertex, [])
            for neighbour in neighbours:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return ans if len(ans) == numCourses else []

            
