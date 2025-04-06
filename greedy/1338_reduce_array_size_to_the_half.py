# Get frequency and sort freq by value in decreasing order. Start removing top frequencies and stop once arr is halved
# O(n) Time and space complexity
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        hashMap = Counter(arr)
        hashMap = sorted(hashMap.values(), reverse=True)
        cumFreq = 0
        for i, freq in enumerate(hashMap):
            cumFreq += freq 
            if cumFreq >= n/2:
                return i + 1

        
