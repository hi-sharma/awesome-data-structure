'''
N = m*n
O(N*2) time and O(N) space complexity
DP (memoization) + DFS
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def is_valid_index(i,j):
            return 0 <= i < n and 0 <=j < m

        def dfs(matrix, i, j):
            if memo[i][j] > 0:
                return memo[i][j]
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            seen = {(i,j)}
            longest_path = 0
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if is_valid_index(x, y) and (x,y) not in seen and matrix[x][y] > matrix[i][j]:
                    seen.add((x,y))
                    if memo[x][y] == 0:
                        memo[x][y] = dfs(matrix, x,y)
                    longest_path = max(longest_path, memo[x][y])
            return longest_path+1

        n = len(matrix)
        m = len(matrix[0])
        ans = 0
        memo = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(matrix, i, j))
        return ans
        
