class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        neg_diagonal = set()
        pos_diagonal = set()
        board = [["."] * n for _ in range(n)]

        res = []

        def backtrack(r):
            if r == n:
                res.append(["".join(board[r]) for r in range(n)])
                return

            for c in range(n):
                if c in cols or r-c in neg_diagonal or r+c in pos_diagonal:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                pos_diagonal.add(r + c)
                neg_diagonal.add(r - c)

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)

        backtrack(0)
        
        return res
