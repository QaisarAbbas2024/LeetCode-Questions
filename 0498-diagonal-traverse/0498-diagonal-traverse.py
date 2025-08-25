from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        ans = [0] * (m * n)
        d = 1  # 1 means moving up-right, -1 means moving down-left
        row, col = 0, 0

        for i in range(m * n):
            ans[i] = matrix[row][col]
            row -= d
            col += d

            # handle out-of-bounds cases
            if row >= m:
                row = m - 1
                col += 2
                d = -d
            if col >= n:
                col = n - 1
                row += 2
                d = -d
            if row < 0:
                row = 0
                d = -d
            if col < 0:
                col = 0
                d = -d

        return ans
