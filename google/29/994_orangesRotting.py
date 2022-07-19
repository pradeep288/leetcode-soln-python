class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        unrotten_tomatoes, rotten_tomatoes = 0, 0

        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_tomatoes += 1
                    q.append([i, j])
                elif grid[i][j] == 1:
                    unrotten_tomatoes += 1
        if unrotten_tomatoes == 0:
            return 0
        if rotten_tomatoes == 0:
            return -1

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while len(q) > 0:
            size = len(q)
            rottened = False
            while size > 0:
                x, y = q.pop(0)
                size -= 1
                for dx, dy in dirs:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                        if grid[new_x][new_y] == 1:
                            rottened = True
                            unrotten_tomatoes -= 1
                            grid[new_x][new_y] = 2
                            q.append([new_x, new_y])
            if rottened:
                time += 1
            if not rottened and unrotten_tomatoes > 0:
                return -1
            elif unrotten_tomatoes == 0:
                return time

        return time
