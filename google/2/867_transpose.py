class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        matrix_t =  [[None] * ROWS for _ in range(COLS)]

        for i in range(ROWS):
            for j in range(COLS):
                matrix_t[j][i] = matrix[i][j]

        return matrix_t
