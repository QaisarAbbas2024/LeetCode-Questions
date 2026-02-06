from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        max_keep = 0
        left = 0
        
        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            max_keep = max(max_keep, right - left + 1)
        
        return n - max_keep
