# 2:44
'''
binary search from 1 to max(nums). Any number >= max(nums) will give len(nums) as answer
O(n*logk) where k = max(nums)
'''
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(mid):
            ans = 0
            for i in range(len(nums)):
                ans = ans + ceil(nums[i]/mid)
            return ans <= threshold

        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right)//2
            if check(mid):
                # search in left sub arr
                right = mid -1
            else:
                # search in right sub arr
                left = mid + 1
        return left
        
