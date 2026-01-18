class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # prefixRow[i][j] = sum of grid[i][0..j-1]
        prefixRow = [[0] * (n + 1) for _ in range(m)]
        # prefixCol[j][i] = sum of grid[0..i-1][j]
        prefixCol = [[0] * (m + 1) for _ in range(n)]

        for i in range(m):
            for j in range(n):
                prefixRow[i][j + 1] = prefixRow[i][j] + grid[i][j]
                prefixCol[j][i + 1] = prefixCol[j][i] + grid[i][j]

        def isMagicSquare(i: int, j: int, k: int) -> bool:
            diag = 0
            antiDiag = 0
            for d in range(k):
                diag += grid[i + d][j + d]
                antiDiag += grid[i + d][j + k - 1 - d]

            if diag != antiDiag:
                return False

            for d in range(k):
                # row sum
                if self._getSum(prefixRow, i + d, j, j + k) != diag:
                    return False
                # column sum
                if self._getSum(prefixCol, j + d, i, i + k) != diag:
                    return False

            return True

        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if isMagicSquare(i, j, k):
                        return k

        return 1

    def _getSum(self, prefix: list[list[int]], idx: int, l: int, r: int) -> int:
        """
        Returns sum of range [l, r) using prefix sums
        """
        return prefix[idx][r] - prefix[idx][l]
