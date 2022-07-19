class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        start_r, start_c, end_r, end_c, empty = 0, 0, 0, 0, 0
        visited = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                elif grid[r][c] == 2:
                    end_r, end_c = r, c
                else:
                    empty += 1
        self.output = 0

        def dfs(r, c, visited, walk):
            if end_r == r and end_c == c:
                if walk + 1 == empty:
                    self.output += 1
                    return

            if 0 <= r < m or 0 <= c < n or grid[r][c] == -1 or (r, c) in visited:
                return

            for dirs in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                visited.add((dirs[0], dirs[1]))
                dfs(r + dirs[0], c + dirs[1])
                visited.remove()

            return self.output

        dfs(0, 0, visited, 0)
