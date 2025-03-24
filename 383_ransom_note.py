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

'''
Time complexity: O(m)
    m is size of magazine. Magazine size > ransomNote size, otherwise we do not have enough characters to construct ransomNote
Space complexity: O(1)
    magazine only has lowercase english letters, so only 26 keys or constant space complexity
'''

