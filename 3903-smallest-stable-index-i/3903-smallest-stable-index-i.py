class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lows = [0] * (n - 1) + [nums[-1]]  # lows[i] = min(nums[i:])
        for i in range(n - 2, -1, -1):
            lows[i] = min(nums[i], lows[i + 1])

        high = nums[0]  # high = max(nums[:i+1])
        for i, x in enumerate(nums):
            high = max(high, x)
            if high - lows[i] <= k:
                return i

        return -1