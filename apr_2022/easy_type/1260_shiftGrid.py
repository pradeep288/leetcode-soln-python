class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp.append(grid[i][j])

        k = k % len(temp)

        temp = temp[len(temp) - k:] + temp[:len(temp) - k]

        idx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = temp[idx]
                idx += 1

        return grid
