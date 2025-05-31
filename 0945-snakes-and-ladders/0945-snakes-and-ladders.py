from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_coordinates(s):
            r = (s - 1) // n
            x = n - 1 - r
            y = (s - 1) % n if r % 2 == 0 else n - 1 - (s - 1) % n
            return x, y

        visited = set()
        queue = deque([(1, 0)])  # (square number, number of moves)

        while queue:
            s, moves = queue.popleft()
            for i in range(1, 7):
                next_s = s + i
                if next_s > n * n:
                    continue
                x, y = get_coordinates(next_s)
                if board[x][y] != -1:
                    next_s = board[x][y]
                if next_s == n * n:
                    return moves + 1
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append((next_s, moves + 1))
        
        return -1
