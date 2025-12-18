from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # Base profit without modification
        base_profit = 0
        for i in range(n):
            base_profit += strategy[i] * prices[i]

        # Prefix sums
        # A[i] = sum of strategy[j] * prices[j] for j < i
        # B[i] = sum of (1 - strategy[j]) * prices[j] for j < i
        A = [0] * (n + 1)
        B = [0] * (n + 1)

        for i in range(n):
            A[i + 1] = A[i] + strategy[i] * prices[i]
            B[i + 1] = B[i] + (1 - strategy[i]) * prices[i]

        best_gain = 0
        half = k // 2

        # Sliding window of size k
        for l in range(n - k + 1):
            mid = l + half
            r = l + k

            # First half becomes 0 (hold)
            gain_first = -(A[mid] - A[l])

            # Second half becomes 1 (sell)
            gain_second = B[r] - B[mid]

            best_gain = max(best_gain, gain_first + gain_second)

        return base_profit + best_gain
