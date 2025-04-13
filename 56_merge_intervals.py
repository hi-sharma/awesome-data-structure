'''
O(nlogn) time and O(n) space complexity
1. Sort on start index
2. Start with  first elem
3. Append other intervals modifying end in place
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > ans[-1][-1]:
                ans.append(intervals[i])
            else:
                end_val = max(ans[-1][-1], intervals[i][-1])
                ans[-1] = [ans[-1][0], end_val]
        return ans
        
