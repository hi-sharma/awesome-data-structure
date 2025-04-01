# Bottom up
# from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # @cache
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for row in range(m):
            for col in range(n):
                if row==col==0:
                    continue
                if row == 0:
                    ans =  dp[row][col-1]
                elif col == 0:
                    ans = dp[row-1][col]
                else: 
                    ans = min(dp[row-1][col], dp[row][col-1])
                dp[row][col] =  grid[row][col] + ans
        return dp[m-1][n-1]
# Top Down
# from functools import cache
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         # @cache
#         def dp(row, col): 
#             if row < 0 or col < 0:
#                 return float("inf")
#             if row == col == 0:
#                 return grid[row][col]
#             if memo[row][col] != -1:
#                 return memo[row][col]
#             memo[row][col] = grid[row][col] + min(dp(row-1, col), dp(row, col -1))
#             return memo[row][col]

#         m = len(grid)
#         n = len(grid[0])
#         memo = [[-1]*n for _ in range(m)]
#         return dp(m-1, n-1)
