class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        max_val = max(nums)

        pos = [(-1, -1) for _ in range(max_val + 1)]

        INF = 1 << 32
        res = INF

        for i, val in enumerate(nums):
            last, second_last = pos[val]

            if second_last != -1:
                distance = (i - second_last) * 2
                res = min(res, distance)

            pos[val] = (i, last)

        return -1 if res == INF else res