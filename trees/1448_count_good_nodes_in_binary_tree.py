# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time and O(n) space complexity
    def goodNodes(self, root: TreeNode) -> int:
        # Iterative solution
        if root is None:
            return 0
        stack = [(root, float("-inf"))]
        ans = 0
        while stack:
            node, maxVal  = stack.pop()
            if node.val >= maxVal:
                ans += 1
            if node.left:
                stack.append([node.left, max(maxVal, node.val)])
            if node.right:
                stack.append([node.right, max(maxVal, node.val)])
        return ans
