from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = set()

        for r in range(m):
            for c in range(n):
                res.add(grid[r][c])  # size 0 rhombus

                k = 1
                while True:
                    if r-k < 0 or r+k >= m or c-k < 0 or c+k >= n:
                        break

                    s = 0
                    
                    # four edges
                    for i in range(k):
                        s += grid[r-k+i][c+i]      # top-right
                        s += grid[r+i][c+k-i]      # right-bottom
                        s += grid[r+k-i][c-i]      # bottom-left
                        s += grid[r-i][c-k+i]      # left-top

                    res.add(s)
                    k += 1

        return sorted(res, reverse=True)[:3]