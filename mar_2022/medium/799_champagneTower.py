class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        glasses = [poured]

        for _ in range(query_row):
            temp = [0] * (len(glasses) + 1)
            for i in range(len(glasses)):
                pour = (glasses[i] - 1) / 2
                if pour > 0:
                    temp[i] += pour
                    temp[i + 1] += pour
            glasses = temp

        return min(1, glasses[query_glass])