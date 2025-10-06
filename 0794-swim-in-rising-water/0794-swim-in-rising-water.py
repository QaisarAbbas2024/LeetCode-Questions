import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        ans = grid[0][0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_heap = [(grid[0][0], 0, 0)]  # (height, i, j)
        seen = [[False] * n for _ in range(n)]
        seen[0][0] = True

        while min_heap:
            height, i, j = heapq.heappop(min_heap)
            ans = max(ans, height)
            if i == n - 1 and j == n - 1:
                return ans
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n and not seen[x][y]:
                    heapq.heappush(min_heap, (grid[x][y], x, y))
                    seen[x][y] = True

        return ans
