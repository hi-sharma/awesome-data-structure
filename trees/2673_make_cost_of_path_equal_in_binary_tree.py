'''
Recusively check
'''
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        def dfs(i):
            if i >= n:
                return 0
            leftcost = dfs(2*i+1)
            rightcost = dfs(2*i + 2)
            self.result += abs(leftcost - rightcost)
            return cost[i] + max(leftcost, rightcost)
        self.result = 0
        dfs(0)
        return self.result
        
        
