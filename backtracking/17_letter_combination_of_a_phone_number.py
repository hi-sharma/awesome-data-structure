class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # O(n* 4^n) time and O(n) space complexity
        def backtrack(curr, i):
            if len(curr) == len(digits):
                ans.append(("").join(curr[:]))
                return

            for j in range(i, len(digits)):
                letters = hashMap[digits[j]]
                for letter in letters:
                    curr.append(letter)
                    backtrack(curr, j+1)
                    curr.pop()    
        
            # Do something
        if len(digits)==0:
            return []

        hashMap = {"2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"],}
        ans = []
        backtrack([], 0)
        return ans    
    
