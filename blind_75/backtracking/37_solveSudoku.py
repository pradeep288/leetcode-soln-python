from collections import defaultdict


class Solution(object):
    def solveSudoku(self, board):
        if not board or len(board) == 0:
            return
        self.solve(board, 0, 0)

    def isValidSudoku(self, board) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r / 3, c / 3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r / 3, c / 3)].add(board[r][c])

        return True

    def solve(self, board, i, j):
        if i == 9 and j == 0:
            return True

        if board[i][j] != ".":
            if j + 1 == 9:
                x = i + 1
                y = 0
            else:
                x = i
                y = j + 1
            return self.solve(board, x, y)
        for c in "123456789":
            if self.isValidSudoku(board):
                board[i][j] = c
                if j + 1 == 9:
                    g = i + 1
                    h = 0
                else:
                    g = i
                    h = j + 1
                if self.solve(board, g, h):
                    return True
                else:
                    board[i][j] = "."
        return False
