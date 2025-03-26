class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Sliding Window Approach: size of longest array containing at most one 0. 
        left = 0 # left index of subarray
        curr = 0 # length of 0s in the current subarray
        ans = 0 # longest array with at most one
        for right in range(len(nums)): # right index on subarray
            if nums[right] == 0:
                curr += 1
            while curr > 1:
                # increment left to remove 0s
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left)
        return ans
