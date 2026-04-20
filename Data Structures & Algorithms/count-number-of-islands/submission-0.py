class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        res = 0

        def bfs(x, y):
            grid[y][x] = 'x'

            q = deque()
            q.append((x, y))

            while q:
                len_q = len(q)
                for i in range(len_q):
                    x, y = q.popleft()
                    grid[y][x] = 'x'

                    for dir in dirs:
                        dx, dy = dir
                        if  0 <= x + dx < n and 0 <= y + dy < m and grid[y + dy][x + dx] == "1":
                            grid[y + dy][x + dx] = 'x'
                            q.append((x + dx, y + dy))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue
                res += 1
                bfs(j, i)

        return res