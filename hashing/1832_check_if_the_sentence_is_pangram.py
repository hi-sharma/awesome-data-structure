class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # O(n) time complexity
        # O(m) or O(1) space complexity as m<=26
        return len(set(sentence))==26
