class Solution:
    def makeGood(self, s: str) -> str:
        # O(n) time and O(n) space complexity
        stack = []
        for c in s:
            if not stack: # empty stack
                stack.append(c)
            else: # stack non empty
                if stack[-1].lower() == c.lower() and stack[-1] != c:
                    stack.pop()
                else:
                    stack.append(c)
        return "".join(stack)
