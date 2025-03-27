class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # O(n) time; O(1) space complexity
        cumSum = nums[0]
        ans = 1 - cumSum
        for i in range(1, len(nums)):
            cumSum += nums[i]
            ans = max(ans, 1 - cumSum)
        return max(ans, 1)
