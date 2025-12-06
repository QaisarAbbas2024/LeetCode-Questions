from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        # dp[i] = number of ways to partition first i elements (i from 0..n), dp[0]=1
        dp = [0] * (n + 1)
        pref = [0] * (n + 1)  # pref[i] = sum_{t=0..i} dp[t]
        dp[0] = 1
        pref[0] = 1

        l = 0
        maxdq = deque()  # indices of elements in nonincreasing order
        mindq = deque()  # indices of elements in nondecreasing order

        for r in range(n):
            # add nums[r]
            while maxdq and nums[maxdq[-1]] <= nums[r]:
                maxdq.pop()
            maxdq.append(r)
            while mindq and nums[mindq[-1]] >= nums[r]:
                mindq.pop()
            mindq.append(r)

            # shrink left until window [l..r] has max-min <= k
            while maxdq and mindq and nums[maxdq[0]] - nums[mindq[0]] > k:
                if maxdq[0] == l:
                    maxdq.popleft()
                if mindq[0] == l:
                    mindq.popleft()
                l += 1

            # valid starts are s in [l..r], sum dp[s] where s counts elements before start
            left_pref = pref[l-1] if l - 1 >= 0 else 0
            dp[r+1] = (pref[r] - left_pref) % mod
            pref[r+1] = (pref[r] + dp[r+1]) % mod

        return dp[n] % mod
