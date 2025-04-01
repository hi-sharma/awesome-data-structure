from functools import cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #Top down DP
        @cache
        def dp(row, col):
            if row < 0 or col < 0:
                return 0
            if row == col ==0:
                return 1-obstacleGrid[0][0]
            ans = dp(row,col-1)*(1- obstacleGrid[row][col-1]) + dp(row - 1,col)*(1- obstacleGrid[row-1][col])
            ans = (1-obstacleGrid[row][col])*ans
            return ans
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return dp(m-1, n-1)


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         # bottom up DP. build a dp[i][j] to save the # of paths from [0][0] to [i][j]
#         # O(m*n) time and space complexity
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         dp = [[0]*n for _ in range(m)]
#         dp[0][0] = 1-obstacleGrid[0][0]
#         for row in range(m):
#             for col in range(n):
#                 # recurrence relation dp[row - 1][col] + dp[row][col-1]
#                 if row == col == 0:
#                     continue
#                 # check for row=0 or col =0 separately
#                 if row == 0:
#                     dp[row][col] = dp[row][col-1]*(1- obstacleGrid[row][col-1])
#                 elif col ==0 :
#                     dp[row][col] = dp[row - 1][col]*(1- obstacleGrid[row-1][col])
#                 # handle the obstacle
#                 else:
#                     dp[row][col] = dp[row][col-1]*(1- obstacleGrid[row][col-1]) + dp[row - 1][col]*(1- obstacleGrid[row-1][col])
#                 dp[row][col] = (1-obstacleGrid[row][col])*dp[row][col]
        # return dp[m-1][n-1]

        
