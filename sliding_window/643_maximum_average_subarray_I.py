class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # initialize the window of size k
        curr = sum(nums[:k])
        ans = curr
        # move window of size k one step to the right, include right elem, remove left elem
        for right in range(k, len(nums)):
            curr += nums[right] - nums[right - k]
            ans = max(curr, ans)
        return round(ans/k, 5)
