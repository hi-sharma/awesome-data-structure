from collections import deque
class Solution:
    # O(m*n) time and space complexity
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."
        
        def is_exit(row, col):
            return maze[row][col] == "." and (row==0 or row==m-1 or col==0 or col==n-1)

        m = len(maze)
        n = len(maze[0])
        entrance_row, entrance_col = entrance
        queue = deque([(entrance_row, entrance_col, 0)])
        seen = set((entrance_row, entrance_col))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # start bfs
        while queue:
            row, col, steps = queue.popleft()
            if is_exit(row, col) and [row, col] != entrance:
                return steps
            for dx, dy in directions:
                next_row, next_col = row + dx , col + dy
                if is_valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
        return -1
            


        
        
