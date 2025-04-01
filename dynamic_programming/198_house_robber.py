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
    

        
