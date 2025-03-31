class Solution:
    # O()
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr_string, left_count, right_count):
            if len(curr_string) == 2*n:
                ans.append("".join(curr_string[:]))
                return 
            if left_count < n:
                curr_string.append("(")
                backtrack(curr_string, left_count + 1, right_count)
                curr_string.pop()
            if left_count > right_count:
                curr_string.append(")")
                backtrack(curr_string, left_count, right_count+1)
                curr_string.pop()

        if n==0:
            return ""
        ans = []
        curr_string = ["("]
        left_count = 1
        right_count = 0
        backtrack(curr_string, left_count, right_count)
        return ans
        
