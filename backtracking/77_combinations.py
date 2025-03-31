class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
      #O(k*n! / (n-k)!*k! )time and O(k) space complexity
        def backtrack(curr, i):
            # base case
            if len(curr) == k:
                ans.append(curr[:])

            for j in range(i, n+1):
                curr.append(j)
                backtrack(curr, j+1)
                curr.pop()
            
        ans = []
        backtrack([], 1)
        return ans
      
        
