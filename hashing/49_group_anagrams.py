'''
O(n*k) time and space compexity. k is # of chars in strings, could be <26 if non repeated
1. construct a hashMap with keys as tuple of count of 26 chars () and values as string.
'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for cand in strs:
            count = [0]*26
            for c in cand:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(cand)
        return list(ans.values())
