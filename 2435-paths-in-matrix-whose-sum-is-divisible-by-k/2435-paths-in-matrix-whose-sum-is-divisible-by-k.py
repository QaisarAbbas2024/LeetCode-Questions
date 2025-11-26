from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        # dp[c][r] would be counts for column c in the previous row (r-1)
        dp = [[0] * k for _ in range(n)]
        
        for i in range(m):
            row_dp = [[0] * k for _ in range(n)]
            for j in range(n):
                val = grid[i][j] % k
                if i == 0 and j == 0:
                    row_dp[0][val] = 1
                    continue
                
                # from top (previous row, same column)
                if i > 0:
                    top = dp[j]
                    for rem in range(k):
                        cnt = top[rem]
                        if cnt:
                            new_rem = (rem + val) % k
                            row_dp[j][new_rem] = (row_dp[j][new_rem] + cnt) % MOD
                
                # from left (same row, previous column)
                if j > 0:
                    left = row_dp[j - 1]
                    for rem in range(k):
                        cnt = left[rem]
                        if cnt:
                            new_rem = (rem + val) % k
                            row_dp[j][new_rem] = (row_dp[j][new_rem] + cnt) % MOD
            
            dp = row_dp
        
        return dp[n - 1][0]
