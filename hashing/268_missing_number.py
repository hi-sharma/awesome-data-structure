class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(n) time complexity
        # O(1) Space complexity
        n = len(nums)
        target = n*(n+1) // 2
        return target - sum(nums)
        
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         # O(n) time complexity
#         # O(n) Space complexity
#         # Using hashMaps
#         seen = set(nums)
#         n = len(nums)
#         for i in range(n+1):
#             if i not in seen:
#                 return i
#         return -1
