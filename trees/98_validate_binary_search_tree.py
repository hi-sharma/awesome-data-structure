# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive solution
class Solution:
    # O(n) space and time complexity
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            # base case
            if not node:
                return True
            if not (small < node.val < large):
                return False
            return dfs(node.left, small, node.val) and dfs(node.right, node.val, large)
        
        return dfs(root, float("-inf"), float("inf"))
        
