class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # O( C(9,K)*K) time and O(K) space complexity
        def backtrack(path, curr_sum, i):
            # base case
            if curr_sum == n and len(path)==k:
                ans.append(path[:])
                return
            for j in range(i, 10):
                if curr_sum < n:
                    path.append(j)
                    backtrack(path, curr_sum + j, j+1)
                    path.pop()
        if n < (k*(k+1))/2:
            return []
        ans = []
        backtrack([], 0, 1)
        return ans        
