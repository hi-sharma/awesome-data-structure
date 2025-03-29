from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # O(n) time complexity
        # O(n) space complexity
        count = defaultdict(int)
        count[0] = -1 # k:v is sum: min_index, wherein the 0 is treated as -1
        curr = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr += -1
            else:
                curr += 1
            if curr in count.keys():
                ans = max(ans, i - count[curr])
            else:
                count[curr] = i
        return ans
