# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Do BFS and print the last node.val at each level 
from collections import deque
class Solution:
    # O(n) time and O(n) space complexity
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            elems_at_level = len(queue)
            for i in range(elems_at_level):
                node = queue.popleft()
                left = node.left
                right = node.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
                if i == elems_at_level - 1:
                    ans.append(node.val)
        return ans

        
