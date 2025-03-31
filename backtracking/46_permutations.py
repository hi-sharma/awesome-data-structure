class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # O(n!) time complexity and O(n) space complexity for call stack
        def backtrack(curr):
            if len(curr) == len(nums):
                #create a copy of curr because curr is only a reference to the array's address.
                ans.append(curr[:])
                return
        
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    # backtrack to upper levels of tree after one call is finished, pop the elem and move to next
                    curr.pop()
            
        ans = []
        backtrack([])
        return ans
