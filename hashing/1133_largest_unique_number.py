from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # O(n) time complexity
        # O(n) space complexity
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        ans = -1
        for k,v in count.items():
            if v==1:
                ans = max(ans, k)
        return ans


        
