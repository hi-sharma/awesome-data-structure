class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            k -= 1 - nums[right]
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1
        return right - left + 1
        
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         left = 0 # left index
#         ans = 0 # final answer storing max length of subarrays at each step
#         curr = 0 # num of 0s in the subarray
#         for right in range(len(nums)):
#             if nums[right] == 0:
#                 curr += 1 
#             # increase left counter if constraint is broken
#             while curr > k:
#                 if nums[left] == 0:
#                     curr -= 1
#                 left += 1
#             ans = max(ans, right - left + 1)
#         return ans

        
