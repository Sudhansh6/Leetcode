class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        q = deque([(0, 0, grid[0][0])])
        m, n = len(grid), len(grid[0])

        dp = {}
        dp[(0, 0)] = 0

        res = m + n
        while len(q):
            r, c, d =  q.pop()

            if r == m - 1 and c == n - 1:
                res = min(res, d)

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if dp.get((nr, nc), m*n) <= d:
                        continue 
                    dp[(nr, nc)] = d
                    q.appendleft((nr, nc, d + grid[nr][nc]))
        
        return health > res