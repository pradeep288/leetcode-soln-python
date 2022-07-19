class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(row, col):
            q = [(row, col)]
            while len(q)>0:
                size = len(q)
                while size > 0:
                    r, c = q.pop(0)
                    size -= 1
                    for d in directions:
                        new_r, new_c = r + d[0], c + d[1]
                        if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == "1" and (new_r, new_c) not in visit:
                            q.append((new_r, new_c))
                            visit.add((new_r, new_c))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visit:
                    islands += 1
                    bfs(i, j)

        return islands
