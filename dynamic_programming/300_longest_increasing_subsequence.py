class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP with state i to return len of increasing subsequence ending at index i
        # Bottom up approach with O(n*2) time and O(n) space complexity
        n = len(nums)
        dp = [1]*n
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
