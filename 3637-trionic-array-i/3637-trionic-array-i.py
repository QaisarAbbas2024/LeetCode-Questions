class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)
        i = 0

        # 1) strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False

        # 2) strictly decreasing
        j = i
        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1
        if j == i or j == n - 1:
            return False

        # 3) strictly increasing
        k = j
        while k + 1 < n and nums[k] < nums[k + 1]:
            k += 1

        return k == n - 1
