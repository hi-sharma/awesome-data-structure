from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # O(n) time complexity
        # O(1) space complexity
        count = defaultdict(int)
        ballon_str = ["b", "a", "l", "o", "n"]
        count = {k:0 for k in ballon_str}
        print(count)
        for char in text:
            if char in ballon_str:
                count[char] += 1
        print(count)
        count["l"] //= 2
        count["o"] //=2
        print(count)
        return min(count.values())
        
