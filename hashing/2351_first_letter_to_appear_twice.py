class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # O(n) time complexity
        # O(n) space complexity; Space complexity could be O(1) if we only consider alphabets from English Language
        hashMap = set()
        for char in s:
            if char in hashMap:
                return char
            else:
                hashMap.add(char)
        return ""
