'''
Use DP. Build bottom up by checking palindrome of length 1, 2, 3, ..and so on 
O(n2) time and space complexity
'''
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = [[False]*n for _ in range(n)]
        ans = [0,0]
        for i in range(n):
            # all strs with length 1 are palindrome
            memo[i][i] = True
        for i in range(n-1):
            # update str with length 2 as palindrome
            if s[i] == s[i+1]:
                memo[i][i+1] = True
                ans = [i, i+1]
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and memo[i+1][j-1]:
                    memo[i][j] = True
                    ans = [i, j]
        i, j = ans
        return s[i:j+1]
