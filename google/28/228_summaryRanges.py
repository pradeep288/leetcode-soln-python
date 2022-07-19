class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        s, c, e = nums[0], nums[0], None
        res = []
        for i in nums[1:]:
            c += 1
            if i == c:
                e = i
            else:
                if not e:
                    res.append(str(s))
                else:
                    res.append(str(s) + "->" + (str(e)))
                s=i
                c=i
                e=None
        if not e:
            res.append(str(s))
        else:
            res.append(str(s) + "->" + (str(e)))

        return res
