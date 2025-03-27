class Solution:
    def countElements(self, arr: List[int]) -> int:
        # O(n) space complexity
        # O(1) Time complexity
        seen = set(arr)
        ans = 0
        for x in arr:
            if x+1 in seen:
                ans += 1
        return ans
