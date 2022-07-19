class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set()
        row_len, col_len=len(matrix), len(matrix[0])
        for i in range(row_len):
            for j in range(col_len):
                print(matrix[i][j])
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Update columns
        for i in rows:
            for j in range(col_len):
                matrix[i][j] = 0

        for i in range(row_len):
            for j in cols:
                matrix[i][j] = 0



