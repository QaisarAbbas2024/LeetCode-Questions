from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int,
                               hBars: List[int],
                               vBars: List[int]) -> int:
        gap = min(self._max_continuous_gap(hBars),
                  self._max_continuous_gap(vBars))
        return gap * gap

    def _max_continuous_gap(self, bars: List[int]) -> int:
        res = 2
        running_gap = 2
        bars.sort()
        for i in range(1, len(bars)):
            if bars[i] == bars[i - 1] + 1:
                running_gap += 1
            else:
                running_gap = 2
            res = max(res, running_gap)
        return res
