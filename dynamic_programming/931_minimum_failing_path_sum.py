'''
dp(row, col) -> min_fail_path_sum starting at (row, col). At the end return memo[0][0]
O(n*2) time and space complexity
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # call dp
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        for i in range(m):
            dp[0][i] = matrix[0][i]
        for row in range(1,m):
            for col in range(n):
                up = dp[row-1][col]
                ld = dp[row-1][col+1] if col < n-1 else float('inf')
                rd = dp[row-1][col-1] if col > 0 else float('inf')
                dp[row][col] = matrix[row][col] + min(up, ld, rd)
        return min(dp[m-1])
