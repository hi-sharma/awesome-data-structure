# from functools import cache
from collections import defaultdict
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # @cache
        def dp(i, holding):
            # base case
            if i >= len(prices):
                return 0
            # recursion case
            if i in memo and holding in memo[i]:
                return memo[i][holding]
            ans = dp(i+1, holding)
            if holding:
                memo[i][holding] = max(ans, prices[i] - fee + dp(i+1, False))
            else:
                memo[i][holding] = max(ans, -prices[i] + dp(i+1, True))
            return memo[i][holding]
        # call dp
        memo = defaultdict(dict)
        return dp(0, False)
        
