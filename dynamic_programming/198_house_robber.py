class Solution:
    def rob(self, nums: List[int]) -> int:
        # Use DP with bottom up approach: O(n) time and space complexity
        n = len(nums)
        if n==1:
            return nums[0]
        robFrom = [0]*(n+1)
        # base case
        robFrom[n] = nums[n-1]
        robFrom[n-1] = max(nums[n-1], nums[n-2])
        # dp[i] = max(dp[i] + robFrom(dp[i+2], db[i+1])
        for i in range(n-2, -1, -1):
            robFrom[i] = max(nums[i] + robFrom[i+2], robFrom[i+1])
        return robFrom[0]
    


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Use DP with top down approach: O(n) time and space complexity
        def robFrom(nums, i):
            n = len(nums)
            # base cases
            if i >= n:
                return 0
            if i in self.memo:
                return self.memo[i]
            # call recursion with memoization
            self.memo[i] = max(nums[i] + robFrom(nums, i+2), robFrom(nums, i+1))
            return self.memo[i]
        self.memo = {}
        return robFrom(nums, 0)
    

        
