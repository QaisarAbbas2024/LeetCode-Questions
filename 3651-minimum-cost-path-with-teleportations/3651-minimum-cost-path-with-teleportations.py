import heapq
from collections import defaultdict

class Solution:
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        INF = 10**18

        # Group cells by value
        value_cells = defaultdict(list)
        for i in range(m):
            for j in range(n):
                value_cells[grid[i][j]].append((i, j))

        sorted_vals = sorted(value_cells.keys())

        # dist[r][c][t]
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0

        # For each teleport count, track which values are unlocked
        unlock_ptr = [0] * (k + 1)

        pq = [(0, 0, 0, 0)]  # cost, r, c, t

        while pq:
            cost, r, c, t = heapq.heappop(pq)
            if cost != dist[r][c][t]:
                continue

            if r == m - 1 and c == n - 1:
                return cost

            # Normal moves
            if r + 1 < m:
                nc = cost + grid[r + 1][c]
                if nc < dist[r + 1][c][t]:
                    dist[r + 1][c][t] = nc
                    heapq.heappush(pq, (nc, r + 1, c, t))

            if c + 1 < n:
                nc = cost + grid[r][c + 1]
                if nc < dist[r][c + 1][t]:
                    dist[r][c + 1][t] = nc
                    heapq.heappush(pq, (nc, r, c + 1, t))

            # Teleport sweep
            if t < k:
                while unlock_ptr[t] < len(sorted_vals) and sorted_vals[unlock_ptr[t]] <= grid[r][c]:
                    v = sorted_vals[unlock_ptr[t]]
                    for x, y in value_cells[v]:
                        if cost < dist[x][y][t + 1]:
                            dist[x][y][t + 1] = cost
                            heapq.heappush(pq, (cost, x, y, t + 1))
                    unlock_ptr[t] += 1

        return -1
