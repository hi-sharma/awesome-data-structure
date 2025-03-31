class Solution:
    #O(n*m) time and space complexity
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # checks if i, j is in bounds and is part of islann
        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] == 1 
        
        def dfs(row, col):
            area = 1
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if is_valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    area += dfs(next_row, next_col)
            return area                    

        m = len(grid)
        n = len(grid[0])
        ans = 0
        seen = set()
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in seen:
                    seen.add((i,j))
                    component_area = dfs(i, j) 
                    # component_area = 1 + dfs(i,j) # dfs: shall return area of island
                    print(f"i:{i}, j:{j}, component_area:{component_area}, ans:{ans}")
                    ans = max(ans, component_area)
        return ans



        
