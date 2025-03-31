class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):
            # do something
            if i > len(nums):
                return
            ans.append(curr[:])
            for i in range(i, len(nums)):
                num = nums[i]
                curr.append(num)
                backtrack(curr, i+1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans
