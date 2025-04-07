# create two stacks, one for ( and another for *
# O(n) time and O(n) space complexity
from collections import defaultdict
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = list()
        wildcard_stack = list()
        for i in range(len(s)):
            if s[i]=='(':
                open_stack.append(i)
            elif s[i] == '*':
                wildcard_stack.append(i)
            else:
                if len(open_stack)>0:
                    _ = open_stack.pop()
                elif len(wildcard_stack)>0:
                    _ = wildcard_stack.pop()
                else:
                    return False
        while open_stack and wildcard_stack:
            if wildcard_stack.pop() < open_stack.pop():
                return False
        return len(open_stack)==0
        
