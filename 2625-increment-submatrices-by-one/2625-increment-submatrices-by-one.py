class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        ans = [[0] * n for _ in range(n)]
        prefix = [[0] * (n + 1) for _ in range(n)]

        # Apply difference array updates
        for row1, col1, row2, col2 in queries:
            for i in range(row1, row2 + 1):
                prefix[i][col1] += 1
                prefix[i][col2 + 1] -= 1

        # Build final matrix using prefix sums
        for i in range(n):
            curr = 0
            for j in range(n):
                curr += prefix[i][j]
                ans[i][j] = curr

        return ans
