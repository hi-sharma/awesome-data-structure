'''
O(n*logn) time and O(n) space complexity
Sort by end index, iterate and update ans if last recorded end index < curr start index 
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        ans = 1
        burstIndex = points[0][-1]
        i = 1
        for x_start, x_end in points:
            if burstIndex < x_start:
                ans += 1
                burstIndex = x_end
        return ans
