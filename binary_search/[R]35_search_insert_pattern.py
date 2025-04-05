class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                # search in left sub arr
                right = mid - 1 
            elif target > nums[mid]:
                # search in right sub arr
                left = mid + 1
            else:
                return mid
        # left is the insert position for order to be maintained
        return left
        
