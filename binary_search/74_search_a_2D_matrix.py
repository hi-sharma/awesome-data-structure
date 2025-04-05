class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Imagine m*n - 1 flattened arr. row_num = index//num_col and col_num = index % num_cols. 
        NO NEED TO DIVIDE BY ROW
        '''
        def get_row_col(index):
            row = index//n
            col = index % n
            return row, col
        m = len(matrix) # num_rows
        n = len(matrix[0]) # num_cols
        left = 0
        right = m*n - 1
        while left <= right:
            mid = (left + right) // 2
            mid_row, mid_col = get_row_col(mid)
            if target < matrix[mid_row][mid_col]:
                # search in left sub arr
                right = mid - 1
            elif target > matrix[mid_row][mid_col]:
                # search in right sub arr
                left = mid + 1
            else:
                return True
        return False
        
