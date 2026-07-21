class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        w = len(word)
        m = len(board)  # rows
        n = len(board[0])  # columns

        def backtrack(pos, index):
            i, j = pos
            if index == w:
                return True
               #out of bounds check                  #char different               #already visited
            if i < 0 or j < 0 or i >= m or j >= n or word[index] != board[i][j] or (i, j) in path:
                return False

            path.add((i, j))

            res = (
                backtrack((i + 1, j), index + 1)
                or backtrack((i - 1, j), index + 1)
                or backtrack((i, j+1), index + 1)
                or backtrack((i, j-1), index + 1)
                )

            path.remove((i,j))
            return res

        for i in range(m):
            for j in range(n):
               if backtrack((i,j),0): return True

        return False




