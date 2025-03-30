# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # O(n) space and time complexity recursive solution
        if not root:
            return 0
        max_so_far = root.val
        min_so_far = root.val
        self.ans = 0
        def dfs(root, max_so_far, min_so_far):
            if root is None:
                return 0
            # update ans
            self.ans = max(self.ans, max(abs(root.val - max_so_far), abs(root.val - min_so_far)))
            max_so_far = max(max_so_far, root.val)
            min_so_far = min(min_so_far, root.val)
            dfs(root.left, max_so_far, min_so_far)
            dfs(root.right, max_so_far, min_so_far)
        dfs(root, max_so_far, min_so_far)
        return self.ans

            
        
        
