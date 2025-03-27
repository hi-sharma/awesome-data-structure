class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # O(n) time complexity
        # O(n) space complexity
        hashMap = set()
        for char in s:
            if char in hashMap:
                return char
            else:
                hashMap.add(char)
        return ""
