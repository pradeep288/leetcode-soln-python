class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = [start]

        while len(q) > 0:
            size = len(q)
            while size > 0:
                cur_index = q.pop(0)
                if arr[cur_index] == 0:
                    return True
                if cur_index + arr[cur_index] < len(arr) and arr[cur_index + arr[cur_index]] != -1:
                    q.append(cur_index + arr[cur_index])
                if cur_index - arr[cur_index] >= 0 and arr[cur_index - arr[cur_index]] != -1:
                    q.append(cur_index - arr[cur_index])
                arr[cur_index] = -1

        return False
