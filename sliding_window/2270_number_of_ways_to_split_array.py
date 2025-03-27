class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Efficient than prefix sum array, O(n) runtime, O(1) space. Do it in one shot
        leftSum = ans = 0
        rightSum = sum(nums)
        for i in range(len(nums)-1):
            leftSum += nums[i]
            rightSum -= nums[i]
            if leftSum >= rightSum:
                ans += 1
        return ans
            


# Using prefix sum
# class Solution:
#     def waysToSplitArray(self, nums: List[int]) -> int:
#         # create a prefix array
#         prefix = [nums[0]]
#         for i in range(1, len(nums)):
#             prefix.append(nums[i] + prefix[i-1])
#         ans = 0
#         for i in range(1, len(nums)):
#             #left : 0 to i-1; right: i to len(nums)-1
#             if prefix[i-1] >= prefix[-1] - prefix[i] + nums[i]:
#                 ans += 1
#         return ans
