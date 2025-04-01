class Solution:
    # from functools import cache
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top down approach O(n) space and O(n) time complexity
        # construct a func dp(i) and return min cost to reach index i. dp(len(cost)) is ans
        # @cache
        def dp(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
            return memo[i]
        
        memo = {}
        return dp(len(cost))


        
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         # bottom up approach O(1) space and O(n) time complexity
#         # construct this dp arr where i (state) is min cost to reach index i. dp[-1] is ans
#         n = len(cost)
#         back_one = back_two = 0
#         for i in range(2, n+1):
#             back_one, back_two = min(back_one + cost[i-1], back_two + cost[i-2]), back_one
#         return back_one
