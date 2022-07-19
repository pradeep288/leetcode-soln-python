class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

        def count_neighbour(i, j):
            count = 0
            for d in dirs:
                x, y = d
                new_x, new_y = r + x, c + y
                if new_x < 0 or new_y < 0 or new_x >= ROWS or new_y >= COLS:
                    continue
                if board[new_x][new_y] in [1, 3]:
                    count += 1
            return count

        for r in range(ROWS):
            for c in range(COLS):
                neighbours = count_neighbour(r, c)
                if board[r][c]:
                    if neighbours in [2, 3]:
                        board[r][c] = 3
                elif neighbours == 3:
                    board[r][c] = 2

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c]in [2, 3]:
                    board[r][c] = 1
