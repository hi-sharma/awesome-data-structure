class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP with bottom up
        # dp array[i] which takes i/states is the amount and return the min # of coins that you need to make that amount
        # Space complexity O(amount) and time complexity O(amount*len(coins))
        n = len(coins)
        dp = [float('inf')]*(amount+1)
        # base case
        dp[0] = 0
        # recurrence relation
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - coin])
        
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]


# # from functools import cache
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # DP with top down/ recursion + memo to save on repeated computations
#         # dp func(i) which takes i/states is the amount and return the min # of coins that you need to make that amount
#         # use memoisation to save states from 0 to amount. 
#         # Space complexity O(amount) and time complexity O(amount*len(coins))
#         # @cache
#         def dp(i):
#             # base case
#             if i < 0:
#                 return float("inf")
#             if i == 0:
#                 return 0
#             if i in memo:
#                 return memo[i]
#             # recurrence relation            
#             memo[i] = min([1 + dp(i-coin) for coin in coins])
#             return memo[i]

#         # call the dp and return
#         memo = {}
#         ans = dp(amount)
#         if ans == float("inf"):
#             return -1
#         return ans
