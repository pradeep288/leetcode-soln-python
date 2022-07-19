import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if grid[0][0]:
            return -1

        visited = set()

        q = collections.deque()

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]

        q.append((0, 0, 1))

        while q:
            r, c, count = q.popleft()

            if r == c == rows:
                return count

            for dr, dc in directions:
                next_r = r + dr
                next_c = c + dc
            if (next_r, next_c) not in visited and 0 <= next_r <= rows and 0 <= next_c <= cols and grid[next_r][
                next_c] == 0:
                visited.add(next_r, next_c)
                q.append((next_r, next_c, count + 1))

        return -1
