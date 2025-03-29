class Solution:
    def simplifyPath(self, path: str) -> str:
        # O(n) runtime and O(n) space complexity
        stack = []
        for portion in path.split("/"):
            if portion == "":
                continue
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                continue
            else:
                stack.append(portion)
        final_path = "/" + "/".join(stack)
        return final_path
