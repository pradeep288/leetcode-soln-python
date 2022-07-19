class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        valley_start, valley_end = 0, 0
        mountain_exists, valley_exists = False, False

        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                mountain_exists = True
            else:
                valley_start = i
                break

        for i in range(valley_start, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                valley_exists = True
                valley_end = i
            else:
                break

        print(mountain_exists, valley_exists, valley_end, len(arr) - 1)

        return mountain_exists and valley_exists and valley_end == len(arr) - 2
