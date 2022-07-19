class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                self.prefix_sum[r + 1][c + 1] = prefix + self.prefix_sum[r][c + 1]
        print(self.prefix_sum)

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, r2, c1, c2 = r1 + 1, r2 + 1, c1 + 1, c2 + 1
        bottom_right = self.prefix_sum[r2][c2]
        top_right = self.prefix_sum[r1 - 1][c2]
        top_left = self.prefix_sum[r1 - 1][c1 - 1]
        bottom_left = self.prefix_sum[r2][c1 - 1]

        return bottom_right - top_right - bottom_left + top_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
