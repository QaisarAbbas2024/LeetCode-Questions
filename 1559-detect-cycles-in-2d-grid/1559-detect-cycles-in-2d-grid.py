class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n=len(grid),len(grid[0])
        visited=set()
        for i in range(0,m):
            for j in range(0,n):
                if (i,j) not in visited:
                    taken={(i,j)}
                    queue=deque()
                    queue.append((i,j))
                    while(queue):
                        i,j=queue.popleft()
                        visited.add((i,j))
                        taken.discard((i,j))
                        for a,b in [[0,-1],[-1,0],[1,0],[0,1]]:
                            x,y=i+a,j+b
                            if 0<=x<m and 0<=y<n and grid[i][j]==grid[x][y] and (x,y) not in visited:
                                if (x,y) in taken:
                                    return True
                                queue.append((x,y))
                                taken.add((x,y))
        return False