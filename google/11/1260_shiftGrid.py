class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                temp.append(grid[i][j])

        k = k % (ROWS * COLS)

        temp = temp[len(temp) - k:] + temp[:len(temp) - k]

        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                grid[i][j] = temp[count]
                count += 1

        return grid
