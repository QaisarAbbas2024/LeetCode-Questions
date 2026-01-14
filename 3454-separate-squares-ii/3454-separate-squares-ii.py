from typing import List, Tuple


class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1  # number of segments
        self.coveredCount = [0] * (4 * self.n)
        self.coveredWidth = [0] * (4 * self.n)

    # Adds val to the range [i, j]
    def add(self, i: int, j: int, val: int) -> None:
        self._add(0, 0, self.n - 1, i, j, val)

    # Returns the covered width of xs[0..n-1]
    def getCoveredWidth(self) -> int:
        return self.coveredWidth[0]

    def _add(self, treeIndex: int, lo: int, hi: int,
             i: int, j: int, val: int) -> None:
        if j <= self.xs[lo] or self.xs[hi + 1] <= i:
            return

        if i <= self.xs[lo] and self.xs[hi + 1] <= j:
            self.coveredCount[treeIndex] += val
        else:
            mid = (lo + hi) // 2
            self._add(2 * treeIndex + 1, lo, mid, i, j, val)
            self._add(2 * treeIndex + 2, mid + 1, hi, i, j, val)

        if self.coveredCount[treeIndex] > 0:
            self.coveredWidth[treeIndex] = self.xs[hi + 1] - self.xs[lo]
        elif lo == hi:
            self.coveredWidth[treeIndex] = 0
        else:
            self.coveredWidth[treeIndex] = (
                self.coveredWidth[2 * treeIndex + 1]
                + self.coveredWidth[2 * treeIndex + 2]
            )


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events: List[Tuple[int, int, int, int]] = []  # (y, delta, xl, xr)
        xs = set()

        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs.add(x)
            xs.add(x + l)

        events.sort()
        xs = sorted(xs)

        halfArea = self.getArea(events, xs) / 2.0
        area = 0
        prevY = 0

        tree = SegmentTree(xs)

        for y, delta, xl, xr in events:
            coveredWidth = tree.getCoveredWidth()
            areaGain = coveredWidth * (y - prevY)

            if area + areaGain >= halfArea:
                return prevY + (halfArea - area) / coveredWidth

            area += areaGain
            tree.add(xl, xr, delta)
            prevY = y

        raise RuntimeError("Should not reach here")

    # Returns the total area of the rectangles
    def getArea(self, events: List[Tuple[int, int, int, int]],
                xs: List[int]) -> int:
        totalArea = 0
        prevY = 0
        tree = SegmentTree(xs)

        for y, delta, xl, xr in events:
            totalArea += tree.getCoveredWidth() * (y - prevY)
            tree.add(xl, xr, delta)
            prevY = y

        return totalArea
