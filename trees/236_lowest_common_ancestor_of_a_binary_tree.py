# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # recursive soln, O(n) space and time complexity
        if not root:
            return None
        
        if root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        return right
# '''
# Find path to n1 and n2 and store in two arrays. Traverse these to get the common ancector
# '''
# def get_path(root, node, path):
#     if root is None:
#         return False
#     path.append(root)
#     if root.val == node.val:
#         return True
#     if (root.left is not None and get_path(root.left, node, path) is not None) or (root.right is not None and get_path(root.right, node, path) is not None):
#         return True
#     path.pop()
#     return False
    
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         path1 = []
#         if not get_path(root, q, path1):
#             return -1
#         print([item.val for item in path1])
#         path2 = []
#         if not get_path(root, p, path2):
#             return -1
#         print([item.val for item in path2])
#         i=0
#         while i < len(path2) and i < len(path2):
#             if path1[i].val != path2[i].val:
#                 break
#             i += 1
#         return path1[i-1]
        
