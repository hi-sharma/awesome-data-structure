# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Iterative solution
class Solution:
    #O(H) time and O(1) space complexity
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_diff = float("inf")
        min_node = float("inf")
        stack = [root]
        while stack:
            node = stack.pop()
            if abs(target - node.val) < min_diff:
                min_diff, min_node = abs(target - node.val), node.val
            elif abs(target - node.val) == min_diff:
                min_diff, min_node =  abs(target - node.val), min(node.val, min_node)
            else: 
                pass
            if target < node.val and node.left:
                stack.append(node.left)
            elif target > node.val and node.right:
                stack.append(node.right)
        return min_node

    # class Solution:
    # def closestValue(self, root: TreeNode, target: float) -> int:
    #     closest = root.val
    #     while root:
    #         closest = min(root.val, closest, key = lambda x: (abs(target - x), x))
    #         root = root.left if target < root.val else root.right
    #     return closest
