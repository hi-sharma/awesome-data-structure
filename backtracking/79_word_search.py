class Solution:
    # O(n*m*3^k) time complexity and O(k) space complexity

    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def backtrack(row, col, i, seen):
            # Base case
            if i == len(word):
                return True

            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if is_valid(next_row, next_col) and board[next_row][next_col] == word[i] and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    if backtrack(next_row, next_col, i+1, seen):
                        return True
                    seen.remove((next_row, next_col))
            return False
        
        directions = [(0,-1), (-1, 0), (0,1), (1,0)]
        seen = set()
        m = len(board)
        n = len(board[0])
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and backtrack(row, col, 1, {(row,col)}):
                    return True
        return False

        
