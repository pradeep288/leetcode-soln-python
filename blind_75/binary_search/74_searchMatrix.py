class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        # Identify the ROW where the element may exist
        row = 0
        while top <= bottom:
            row = top + (bottom - top) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break

        if top > bottom:
            return False

        l, h = 0, len(matrix[0])

        while l <= h:
            m = l + ((h - l) // 2)
            if matrix[row][m] == target:
                return True

            if matrix[row][m] > target:
                h = m - 1
            else:
                l = m + 1

        return False
