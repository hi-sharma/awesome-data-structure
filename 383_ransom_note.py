class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # from collections import Counter
        # freq_map = Counter(magazine)
        freq_map = {}
        for char in magazine:
            freq_map[char] = freq_map.get(char, 0) + 1
        for note in ransomNote:
            if freq_map.get(note, 0) > 0:
                freq_map[note] -= 1
            else:
                return False
        return True

'''
{a : 1}
{a : 1, b: 1}
{"a": 2, "b": 1}
'''
