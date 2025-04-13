'''
O(n) time and O(n) space complexity
1. Use hashMap to store freq of prefix[i] sum.
2. Iterate over arr, building prefix sum and checking existence/freq. of runninSum-k encountered till index 
'''
from collections import defaultdict 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        hashMap[0] = 1
        runningSum = 0
        ans = 0
        for i in range(len(nums)):
            runningSum +=  nums[i]
            ans += hashMap[runningSum - k]
            hashMap[runningSum] += 1
        return ans
