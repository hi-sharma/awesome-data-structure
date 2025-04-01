class Solution:
    def climbStairs(self, n: int) -> int:
        # Top down DP approach. O(n) time complexity and O(n) space complexity
        if n <= 2:
            return n
        prev_prev_step = 1
        prev_step = 2
        for i in range(3, n+1):
            prev_step, prev_prev_step = prev_step + prev_prev_step,prev_step
        return prev_step

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # Bottom up DP approach. O(n) time complexity and O(n) space complexity
#         def dp(i):
#             # base case
#             if i<=2:
#                 return i
#             # recurrence relation
#             if i in memo:
#                 return memo[i]
#             memo[i] = dp(i-1) + dp(i-2)
#             return memo[i]
#         # call dp
#         memo = {}
#         return dp(n)
