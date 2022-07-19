class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited, q = set(), []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Find out all the border regions which are not captured
        for i in range(ROWS):
            for j in range(COLS):
                if (i in [0, ROWS - 1] or j in [0, COLS - 1]) and board[i][j] == "O":
                    q.append((i, j))

        while len(q) > 0:
            size = len(q)
            while size:
                r, c = q.pop(0)
                size -= 1
                visited.add((r, c))
                board[r][c] = "T"
                for d in directions:
                    new_r, new_c = r + d[0], c + d[1]
                    print(new_r, new_c)
                    if (0 <= new_r < ROWS and 0 <= new_c < COLS) and ((new_r, new_c) not in visited) and board[new_r][
                        new_c] == "O":
                        q.append((new_r, new_c))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
