class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0 
        left = 0
        curr_prd = 1
        if k <= 1:
            return 0
        for right in range(len(nums)):
            curr_prd *= nums[right]
            while curr_prd >= k: #and left < right:
                curr_prd //= nums[left]
                left += 1
            # if curr_prd < k:
            ans = ans + (right - left + 1)
        return ans



        
