class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        row_start = 0
        row_end = rows - 1
        while row_start <= row_end:
            row_mid = (row_start + row_end) // 2
            if target >= matrix[row_mid][0] and target <= matrix[row_mid][-1]:
                col_start = 0
                col_end = len(matrix[row_mid]) - 1
                while col_start <= col_end:
                    col_mid = (col_start + col_end) // 2
                    if target == matrix[row_mid][col_mid]:
                        return True
                    elif target < matrix[row_mid][col_mid]:
                        col_end = col_mid - 1
                    else:
                        col_start = col_mid + 1
                return False
            elif target < matrix[row_mid][0]:
                row_end = row_mid - 1
            else:
                row_start = row_mid + 1

        return False