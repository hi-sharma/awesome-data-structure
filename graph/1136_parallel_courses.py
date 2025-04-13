'''
O(N+E) space and time complexity
1. Maintaing adj_list, indegree arr and queue. Put indegree with val.
'''
from collections import deque
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # build adjacency list
        adj_list = [[] for i in range(n)]
        indegree = [0]*(n)
        # save as 0 indexed
        for i in range(len(relations)):
            prevCourse, nextCourse = relations[i]
            adj_list[prevCourse-1].append((nextCourse-1))
            indegree[nextCourse-1] += 1
        # build indegree arr and initialize queue
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                # seen.add(i)
        # while queue is non empty: visit nodes, update ans, update course visited, update queue
        numSemester = 0
        numCourses = 0
        # print(queue)
        # print(indegree)
        while queue:
            queue_len = len(queue)
            numSemester += 1
            numCourses += queue_len 
            for i in range(queue_len):
                course = queue.popleft()
                # seen.add(course)
                # print(course, seen, numSemester, nextCourseList, indegree)
                for i in range(len(indegree)):
                    if i in adj_list[course]:
                        indegree[i] -= 1
                        if indegree[i]==0:
                            queue.append(i)
        if numCourses == n:
            return numSemester
        return -1        
