import math
# O(L) space and time complexity
class Solution:
    def maximum69Number (self, num: int) -> int:
        arr = []
        while num > 0:
            arr.append(num % 10)
            num = num // 10
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 6:
                arr[i] = 9
                break
        ans = 0
        for i in range(len(arr)):
            ans += arr[i]*math.pow(10,i)
        return int(ans)
