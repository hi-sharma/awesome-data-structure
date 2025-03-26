class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # neg_pointer, pos_pointer = 0,0
        ans = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                neg_pointer = i - 1
                pos_pointer = i
                break
            else:
                neg_pointer = i 
                pos_pointer = i + 1

        while neg_pointer >= 0 and pos_pointer < len(nums):
            if abs(nums[neg_pointer]) < abs(nums[pos_pointer]):
                ans.append(nums[neg_pointer]**2)
                neg_pointer -= 1
            else:
                ans.append(nums[pos_pointer]**2)
                pos_pointer += 1
        while neg_pointer >= 0:
            ans.append(nums[neg_pointer]**2)
            neg_pointer -= 1
        while pos_pointer < len(nums):
            ans.append(nums[pos_pointer]**2)
            pos_pointer += 1
        return ans

        
