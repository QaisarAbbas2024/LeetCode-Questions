class Solution:
    def maxSumDivThree(self, nums):
        dp = [0, 0, 0]  # dp[i] = max sum so far such that sum % 3 == i

        for num in nums:
            for s in dp.copy():
                dp[(s + num) % 3] = max(dp[(s + num) % 3], s + num)

        return dp[0]
