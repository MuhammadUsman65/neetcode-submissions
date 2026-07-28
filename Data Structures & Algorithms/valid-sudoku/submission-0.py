class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #validate rows
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
                
        #validate cols
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        #validate boxes
        for box in range(9):
            s = set()
            start_row = (box // 3) * 3
            start_col = (box % 3) * 3
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    item = board[r][c]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)

        return True