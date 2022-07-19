class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        one_dimension_matrix = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                one_dimension_matrix.append(matrix[i][j])

        l, h = 0, len(one_dimension_matrix) - 1

        while l <= h:
            m = l + (h - l) // 2
            if one_dimension_matrix[m] == target:
                return True
            if one_dimension_matrix[m] > target:
                h = m - 1
            else:
                l = m + 1

        return False
