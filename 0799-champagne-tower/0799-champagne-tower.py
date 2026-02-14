class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * (query_row + 1)
        dp[0] = float(poured)

        for i in range(query_row):
            new_dp = [0.0] * (query_row + 1)
            for j in range(i + 1):
                if dp[j] > 1:
                    overflow = (dp[j] - 1) / 2.0
                    new_dp[j] += overflow
                    new_dp[j + 1] += overflow
            dp = new_dp

        return min(1.0, dp[query_glass])
