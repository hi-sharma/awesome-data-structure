class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        #O(2^n)  time and space complexity
        def convert_to_num(arr, n):
            out = 0
            for i in range(n):
                out += arr[i]*(10**(n-i-1))
            return out

        def backtrack(curr):
            if len(curr) == n:
                ans.append(curr[:])
                return
            for new_digit in range(10):
                # if no elem in curr, add the elem
                if len(curr) == 0:
                    # skip 0 for first digit
                    if new_digit==0:
                        continue
                    curr.append(new_digit)
                    backtrack(curr)
                    curr.pop()

                # check diff of last digit and new_digit to be == k
                elif abs(curr[-1] - new_digit) == k:
                    curr.append(new_digit)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return [convert_to_num(sub_arr, n) for sub_arr in ans]
        
