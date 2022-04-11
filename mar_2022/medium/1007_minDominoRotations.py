class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def get_min(arr1, arr2):
            hash_map = {}
            min_val = float('+inf')
            for i in range(len(arr1)):
                if arr1[i] in hash_map.keys():
                    continue
                cur_val, count, swap_count = arr1[i], 0, 0
                for j in range(len(arr1)):
                    if i == j or arr1[j] == cur_val:
                        count += 1
                    elif arr2[j] == cur_val:
                        count += 1
                        swap_count += 1
                if count == len(arr1):
                    min_val = min(min_val, swap_count)
                hash_map[arr1[i]] = min_val

            return min_val

        top_min = get_min(tops, bottoms)
        bottom_min = get_min(bottoms, tops)

        if top_min == float('+inf') and bottom_min == float('+inf'):
            return -1

        if top_min != float('+inf') and bottom_min != float('+inf'):
            return min(top_min, bottom_min)
        else:
            if top_min == float('+inf'):
                return bottom_min
            else:
                return top_min
