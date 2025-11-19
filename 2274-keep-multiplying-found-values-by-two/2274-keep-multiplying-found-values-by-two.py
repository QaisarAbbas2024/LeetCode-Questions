class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        seen = set(nums)              # O(n) to build
        while original in seen:       # each check ≈ O(1)
            original *= 2
        return original
