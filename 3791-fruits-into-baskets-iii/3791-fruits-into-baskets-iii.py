from typing import List

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self._build(nums, 0, 0, self.n - 1)

    def _merge(self, left: int, right: int) -> int:
        return max(left, right)

    def _build(self, nums: List[int], tree_index: int, lo: int, hi: int):
        if lo == hi:
            self.tree[tree_index] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(nums, 2 * tree_index + 1, lo, mid)
        self._build(nums, 2 * tree_index + 2, mid + 1, hi)
        self.tree[tree_index] = self._merge(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])

    def update(self, i: int, val: int):
        self._update(0, 0, self.n - 1, i, val)

    def _update(self, tree_index: int, lo: int, hi: int, i: int, val: int):
        if lo == hi:
            self.tree[tree_index] = val
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * tree_index + 1, lo, mid, i, val)
        else:
            self._update(2 * tree_index + 2, mid + 1, hi, i, val)
        self.tree[tree_index] = self._merge(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])

    def query_first(self, target: int) -> int:
        return self._query_first(0, 0, self.n - 1, target)

    def _query_first(self, tree_index: int, lo: int, hi: int, target: int) -> int:
        if self.tree[tree_index] < target:
            return -1
        if lo == hi:
            self.update(lo, -1)  # Mark as used
            return lo
        mid = (lo + hi) // 2
        left_val = self.tree[2 * tree_index + 1]
        if left_val >= target:
            return self._query_first(2 * tree_index + 1, lo, mid, target)
        else:
            return self._query_first(2 * tree_index + 2, mid + 1, hi, target)


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        tree = SegmentTree(baskets)
        count = 0
        for fruit in fruits:
            if tree.query_first(fruit) == -1:
                count += 1
        return count
