class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        maxr = len(grid) - 1
        maxc = len(grid[0]) - 1
        def explore(i,j):
            q = collections.deque()
            q.append((i,j))
            grid[i][j] = '#'
            temp = 1
            while q:
                r, c = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr <= maxr) and (0 <= nc <= maxc) and (grid[nr][nc] == 1):
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        temp += 1
            return temp
        for i in range(maxr + 1):
            for j in range(maxc + 1):
                if grid[i][j] == 1:
                    temp = explore(i,j)
                    if temp > res:
                        res = temp
        return res

