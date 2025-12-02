from typing import List
from collections import Counter

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        # Count how many points at each y-coordinate
        cnt = Counter(y for x, y in points)
        # For every horizontal line y, compute number of ways to choose two points on that line
        pairs = []
        for y, c in cnt.items():
            if c >= 2:
                pairs.append(c * (c - 1) // 2)
        # Now for every pair of distinct horizontal lines, number of trapezoids is product of pairs
        # Sum over all combinations (i, j), i < j
        total = 0
        s = 0
        for p in pairs:
            total = (total + s * p) % MOD
            s = (s + p) % MOD
        return total
