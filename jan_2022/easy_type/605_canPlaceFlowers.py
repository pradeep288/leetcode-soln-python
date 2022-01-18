class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Special Case1:  when number of flowers to plant is 0
        if n == 0:
            return True

        # Special Case2:  when length of flowerbed is 1
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n = n - 1
            return n == 0

        cur_plot = 0

        while cur_plot < len(flowerbed) and n != 0:
            # Special Case3:  When Plot is at left Edge
            if cur_plot == 0:
                if flowerbed[cur_plot] == 0 and flowerbed[cur_plot + 1] == 0:
                    flowerbed[cur_plot] = 1
                    n = n - 1
            # Special Case4:  When Plot is at right Edge
            elif cur_plot == len(flowerbed) - 1:
                if flowerbed[cur_plot] == 0 and flowerbed[cur_plot - 1] == 0:
                    flowerbed[cur_plot] = 1
                    n -= 1
            else:
                if flowerbed[cur_plot - 1] == 0 and flowerbed[cur_plot] == 0 \
                        and flowerbed[cur_plot + 1] == 0:
                    flowerbed[cur_plot] = 1
                    n -= 1
            cur_plot += 1

        return n == 0
