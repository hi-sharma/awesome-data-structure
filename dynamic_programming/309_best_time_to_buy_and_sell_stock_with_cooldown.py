'''
max_profit(skip, buy, sell with cooldown)
DP: return max profit  till index i given cooldown contraints
'''
# from functools import cache
from collections import defaultdict
class Solution:
    # O(N) time and space where is # of states, N = 2*len(prices). So O(n)
    def maxProfit(self, prices: List[int]) -> int:
        # @cache
        def dp(i, holding):
            # base cases
            if i >= len(prices):
                return 0
            if i in memo and holding in memo[i]:
                return memo[i][holding]
            # recurrence relation
            ans = dp(i+1, holding) # skip
            if holding: # sell
                memo[i][holding] = max(ans, prices[i] + dp(i+2, False))
            else: # buy
                memo[i][holding] = max(ans, -prices[i] + dp(i+1, True))
            return memo[i][holding]

        # call the dp 
        memo = defaultdict(dict)
        return dp(0, False)
        
