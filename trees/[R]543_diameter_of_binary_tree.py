# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # same as longest path from a node to left/right or maximum depth of tree
        if root is None:
            return 0
        self.diameter = 0
        def findMaxDepth(node):
            if node is None:
                return 0
            left_depth = findMaxDepth(node.left) 
            right_depth = findMaxDepth(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        findMaxDepth(root)
        return self.diameter
        
