class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        neg_diagonal = set()
        pos_diagonal = set()
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                res.append(1)
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diagonal or (r - c) in neg_diagonal or board[r][c] == "Q":
                    continue
                board[r][c] = "Q"
                cols.add(c)
                pos_diagonal.add(r + c)
                neg_diagonal.add(r - c)

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                pos_diagonal.remove(r + c)
                neg_diagonal.remove(r - c)

        backtrack(0)

        return len(res)
