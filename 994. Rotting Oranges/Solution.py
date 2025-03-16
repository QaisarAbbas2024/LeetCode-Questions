class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows, cols = len(grid), len(grid[0])  # Get grid size
        queue = deque()  # Queue to store rotten oranges
        fresh_count = 0  # Count fresh oranges
        minutes = 0  # Timer for rotting process

        # Step 1: Find all rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  # Rotten orange
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:  # Fresh orange
                    fresh_count += 1

        # Step 2: Define directions for moving (Right, Left, Down, Up)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]  

        # Step 3: Start BFS
        while queue:
            r, c, time = queue.popleft()  # Process one rotten orange
            minutes = time  # Update minutes with last rotting time

            # Check all 4 possible directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Rot the fresh orange
                    fresh_count -= 1   # Reduce fresh orange count
                    queue.append((nr, nc, time + 1))  # Add to queue with updated time

        # Step 4: If any fresh oranges are left, return -1, else return minutes
        return minutes  if fresh_count == 0 else -1
