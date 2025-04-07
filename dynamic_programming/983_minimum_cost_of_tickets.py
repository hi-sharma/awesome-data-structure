from collections import defaultdict
# O(K) time and space complexity where K is max(days)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def solve(currDay):
            if currDay > days[len(days) -1 ]:
                return 0
            if currDay not in isTravelNeeded:
                return solve(currDay + 1)
            if dp[currDay] != -1:
                return dp[currDay] 
            oneDay = costs[0] + solve(currDay + 1)
            sevenDay = costs[1] + solve(currDay + 7)
            thirtyDay = costs[2] + solve(currDay + 30)
            dp[currDay] = min(oneDay, sevenDay, thirtyDay)
            return dp[currDay]

        isTravelNeeded = set(days)
        max_days = days[-1]
        dp = [-1]*(max_days + 1)
        return solve(1)
