# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time and O(n) space complexity
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if node is None:
                return False
            if node.left == None and node.right == None:
                return curr + node.val == targetSum
            curr += node.val
            return dfs(node.left, curr) or dfs(node.right, curr)
        return dfs(root, 0)
        
