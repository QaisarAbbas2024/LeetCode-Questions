class Solution:
    def specialTriplets(self, nums):
        from collections import Counter
        
        MOD = 10**9 + 7
        
        right = Counter(nums)   # counts to the right of j
        left = Counter()        # counts to the left of j
        
        ans = 0
        
        for j in range(len(nums)):
            right[nums[j]] -= 1   # j is now middle
            
            target = nums[j] * 2
            
            if left[target] > 0 and right[target] > 0:
                ans = (ans + left[target] * right[target]) % MOD
            
            left[nums[j]] += 1   # move j to left
        
        return ans % MOD
