class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        twoD_to_oneD_arr = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                twoD_to_oneD_arr.append(matrix[i][j])

        def binary_search(arr, target):
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == target:
                    return True
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False

        return binary_search(twoD_to_oneD_arr, target)
