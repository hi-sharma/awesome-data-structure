# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
O(n) time and O(n) space complexity for recursive call stack
1. Track path of startValue and destValue from root with L and R. Using a list. and do dfs
2. Remove common prefix of startValue and destValue
3. Convert startValue to Us and destValue as
'''
from collections import defaultdict
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, target_value, path):
            # dfs to track path in a list and searchNode as startValue/destValue
            # base case
            if node is None:
                return False
            if node.val == target_value:
                return True
            path.append("L")
            if dfs(node.left, target_value, path):
                return True
            path.pop()
            path.append("R")
            if dfs(node.right, target_value, path):
                return True
            path.pop()
            return False

        start_path = []
        dest_path = []
        dfs(root, startValue, start_path)
        dfs(root, destValue, dest_path)
        pathFromRoot = {"start": start_path,  "end": dest_path}
        common_length = 0
        while common_length < len(pathFromRoot["start"]) and common_length < len(pathFromRoot["end"]) and pathFromRoot["start"][common_length] == pathFromRoot["end"][common_length]:
                common_length += 1
        ans = []
        for i in range(common_length, len(pathFromRoot["start"])):
            ans.append("U")
        for j in range(common_length, len(pathFromRoot["end"])):
            ans.append(pathFromRoot["end"][j])
        return "".join(ans)
        

        
