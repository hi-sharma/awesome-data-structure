class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Create a sorted array in decreasing order
        # Do it in one pass
        n = len(nums) - 1
        ans = [0]*(n+1)
        i, j = 0, n 
        for ind in range(n, -1, -1):
            if i > j:
                break
            if abs(nums[i]) < abs(nums[j]):
                ans[ind] = nums[j]**2
                j -= 1
            else:
                ans[ind] = nums[i]**2
                i += 1
        return ans


# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         # Create a sorted array in decreasing order
#         i = 0 
#         j = len(nums) - 1
#         ans = []
#         while i <= j:
#             if abs(nums[i]) < abs(nums[j]):
#                 ans.append(nums[j]**2)
#                 j -= 1
#             else:
#                 ans.append(nums[i]**2)
#                 i += 1
#         # Reverse the array
#         i = 0
#         j = len(ans) -1 
#         while i < j:
#             ans[i], ans[j] = ans[j], ans[i]
#             i += 1
#             j -= 1
#         return ans

# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         # neg_pointer, pos_pointer = 0,0
#         ans = []
#         for i in range(len(nums)):
#             if nums[i] >= 0:
#                 neg_pointer = i - 1
#                 pos_pointer = i
#                 break
#             else:
#                 neg_pointer = i 
#                 pos_pointer = i + 1

#         while neg_pointer >= 0 and pos_pointer < len(nums):
#             if abs(nums[neg_pointer]) < abs(nums[pos_pointer]):
#                 ans.append(nums[neg_pointer]**2)
#                 neg_pointer -= 1
#             else:
#                 ans.append(nums[pos_pointer]**2)
#                 pos_pointer += 1
#         while neg_pointer >= 0:
#             ans.append(nums[neg_pointer]**2)
#             neg_pointer -= 1
#         while pos_pointer < len(nums):
#             ans.append(nums[pos_pointer]**2)
#             pos_pointer += 1
#         return ans
