from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # O(n) Time complexity
        # O(n) Space complexity
        curr = 0
        ans = 0
        count = defaultdict(int)
        count[0] = 1
        for num in nums:
            curr += num % 2
            ans += count[curr - k]
            count[curr] += 1 
        return ans 

        
