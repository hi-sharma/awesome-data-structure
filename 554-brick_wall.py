'''
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2
Example 2:

Input: wall = [[1],[1],[1]]
Output: 3
Approach
"1. Draw on paper
2. Declare a hashmap collections.defaultdict(int), and count number of bricks ending at each cum_sum. Find the index with most number of lines end, subtract from total array row length"
'''
from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        num_rows = len(wall)
        base_row = wall[0]
        num_indices = sum(base_row)
        end_map = defaultdict(int)
        # end_map = {k:0 for k in range(num_indices)}
        for row in wall:
            cum_sum = row[0]
            end_map[cum_sum-1] += 1
            for j in range(1, len(row)):
                cum_sum += row[j]
                end_map[cum_sum-1] += 1
        max_val = 0
        for item, val in end_map.items():
            if item not in [num_indices-1]:
                max_val = max(val,max_val)
            else:
                continue
        print(end_map)
        return num_rows - max_val
        
