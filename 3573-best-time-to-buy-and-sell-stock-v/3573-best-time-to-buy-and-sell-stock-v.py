from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # dp[j][s]: max profit with at most j transactions
        # and ending in state s (0=neutral, 1=long, 2=short)
        dp = [[0] * 3 for _ in range(k + 1)]

        # Initialize for day 0: 
        # impossible to be in neutral state (0 profit) with holdings
        # but we can buy long or short sell for states 1 and 2
        for j in range(1, k + 1):
            dp[j][1] = -prices[0]
            dp[j][2] = prices[0]

        for i in range(1, n):
            price = prices[i]
            new_dp = [[0] * 3 for _ in range(k + 1)]
            for j in range(1, k + 1):
                # neutral: either stay neutral, close long, or close short
                new_dp[j][0] = max(
                    dp[j][0],
                    dp[j][1] + price,
                    dp[j][2] - price
                )

                # long: either stay long, or buy new (consume one transaction)
                new_dp[j][1] = max(
                    dp[j][1],
                    dp[j - 1][0] - price
                )

                # short: either stay short, or short sell new (consume one transaction)
                new_dp[j][2] = max(
                    dp[j][2],
                    dp[j - 1][0] + price
                )

            dp = new_dp

        return dp[k][0]
