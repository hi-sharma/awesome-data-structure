# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
from collections import deque
class Solution:
    # O(n) time and O(n) space complexity
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        level = 0
        ans = []
        while queue:
            elems_at_level = len(queue)
            level_traversal = []
            for _ in range(elems_at_level):
                node = queue.popleft()
                level_traversal.append(node.val)
                left = node.left
                right = node.right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 1:
                n = len(level_traversal)
                for i in range(n//2):
                    level_traversal[i], level_traversal[n-i-1] = level_traversal[n-i-1], level_traversal[i] 
            ans.append(level_traversal)
            level += 1
        return ans

        
        
