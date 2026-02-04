from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        NEG = -10**30

        up = [NEG] * n       # first increasing
        down = [NEG] * n     # decreasing
        up2 = [NEG] * n      # second increasing

        for i in range(1, n):
            a, b = nums[i - 1], nums[i]

            # phase 1: increasing
            if a < b:
                up[i] = max(a + b, up[i - 1] + b)

            # phase 2: decreasing
            if a > b:
                if up[i - 1] != NEG:
                    down[i] = up[i - 1] + b
                if down[i - 1] != NEG:
                    down[i] = max(down[i], down[i - 1] + b)

            # phase 3: increasing again
            if a < b:
                if down[i - 1] != NEG:
                    up2[i] = down[i - 1] + b
                if up2[i - 1] != NEG:
                    up2[i] = max(up2[i], up2[i - 1] + b)

        return max(up2)
