from collections import defaultdict
class Solution:
    # O(m*n) time and space complexity
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(row, col):
            if row < 0 or col < 0:
                return 0
            if row == 0 and col == 0:
                return 1
            if memo[row][col] != -1:
                return memo[row][col]
            memo[row][col] = dp(row-1, col) + dp(row, col-1) 
            return memo[row][col]
        memo = [[-1]*n for _ in range(m)]
        return dp(m-1, n-1)
