'''
DP: max(nums[i] + dp[i+2], dp[i+1])
O(n) time and space complexity
'''
# from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(start_index, end_index):
            # base case with constraints
            if start_index > end_index:
                return 0
            # recursive case
            if start_index not in memo:
                memo[start_index] = max(nums[start_index] + dp(start_index+2, end_index), dp(start_index+1, end_index))
            result = memo[start_index]
            return result

        if len(nums) <= 2:
            return max(nums)
            
        memo = {}
        ans1 = dp(0, len(nums) - 2)
        memo = {}
        ans2 = dp(1, len(nums) - 1)
        return max(ans1, ans2)


        
