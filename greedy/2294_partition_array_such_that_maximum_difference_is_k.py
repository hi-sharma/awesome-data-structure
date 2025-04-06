'''
Sort and maintain two pointers to count number of partitions. O(nlogn) time and O(n) space for sorting
'''
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end = 0,0
        ans = 0
        while end < len(nums):
            max_diff = nums[end] - nums[start]
            if max_diff <= k:
                end += 1
            else:
                ans += 1
                start = end
        # Add 1 to include final sub arr
        return ans + 1
