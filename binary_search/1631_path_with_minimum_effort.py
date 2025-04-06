# O(m*n*logk) where k = max(heights)
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def check_index(row, col):
            return 0 <= row <= m-1 and 0 <= col <= n-1

        def dfs(effort):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            seen = {(0, 0)}
            stack = [(0, 0)]
            while stack:
                row, col = stack.pop()
                if (row, col) == (m - 1, n - 1):
                    return True
                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if check_index(next_row, next_col) and (next_row, next_col) not in seen:
                        if abs(heights[row][col] - heights[next_row][next_col]) <= effort:
                            stack.append((next_row, next_col))
                            seen.add((next_row, next_col))
            return False

        m = len(heights)
        n = len(heights[0])
        left = 0
        right = max([max(heights[row]) for row in range(m)])
        print(left, right)
        while left <= right:
            mid = (left + right)//2
            check = dfs(mid)
            print(left, mid, right, check)
            if check:
                # search in left sub arr to find min
                right = mid - 1
            else:
                # search in right sub arr to find min
                left = mid + 1
        return left

            
        
