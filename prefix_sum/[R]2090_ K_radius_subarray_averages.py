class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
      #O(n) time and O(1) space complexity
        # Base cases
        n = len(nums)
        if k==0:
            return nums
        if n < (2*k + 1):
            return [-1]*n
        ans = [-1]*n
        subarray_len = 2*k + 1
        cumSum = sum(nums[:subarray_len])
        ans[k] = cumSum//subarray_len
        # Faced issues with respect to indexing
        for i in range(subarray_len, n):
            cumSum = cumSum - nums[i-subarray_len] + nums[i]
            ans[i-k] = cumSum//subarray_len
        return ans

