class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # O(n*2^n) time and O(n) space complexity
        def backtrack(curr, i):
            # do something
            if i > len(nums):
                return
            ans.append(curr[:])
            for j in range(i, len(nums)):
                num = nums[j]
                curr.append(num)
                backtrack(curr, j+1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans
        
