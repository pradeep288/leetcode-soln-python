class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c):
            q = [(r, c)]
            cur_area = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while len(q) > 0:
                size = len(q)
                while size > 0:
                    size -= 1
                    cur_x, cur_y = q.pop(0)
                    if (cur_x, cur_y) in visited:
                        continue
                    cur_area += 1
                    print(cur_area, cur_x, cur_y)
                    visited.add((cur_x, cur_y))
                    for d in directions:
                        x, y = d[0], d[1]
                        new_x, new_y = x + cur_x, y + cur_y
                        if 0 <= new_x < ROWS and 0 <= new_y < COLS and (new_x, new_y) not in visited and grid[new_x][
                            new_y] == 1:
                            q.append((new_x, new_y))

            return cur_area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(bfs(i, j), max_area)

        return max_area
