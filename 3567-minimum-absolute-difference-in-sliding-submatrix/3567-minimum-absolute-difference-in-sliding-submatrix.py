from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                vals = []
                
                # collect k x k elements
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])
                
                # sort values
                vals.sort()
                
                # find min absolute difference
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    if vals[t] != vals[t - 1]:  # distinct values
                        min_diff = min(min_diff, vals[t] - vals[t - 1])
                
                # if all values same → 0
                ans[i][j] = 0 if min_diff == float('inf') else min_diff
        
        return ans