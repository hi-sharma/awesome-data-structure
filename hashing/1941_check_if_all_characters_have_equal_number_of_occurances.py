from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        #O(n) time complexity
        #O(n) space complexity
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        count = {v: k for k, v in count.items()}
        return len(count) == 1            
        
        
