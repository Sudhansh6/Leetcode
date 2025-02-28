class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Using a DFS approach would be wrong because DFS would make the code memoize longer paths without exploring shorter paths!
        m, n = len(grid), len(grid[0])
        q = deque()
        q.appendleft((0, 0, k, 0))
        dp = {}
        while len(q):
            r, c, k2, s = q.pop()
            if s >= dp.get((r, c, k2), m*n):
                continue

            if k2 < 0:
                continue

            if r == m - 1 and c == n - 1:
                return s 

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n:
                    continue 
                q.appendleft((nr, nc, k2 - grid[nr][nc], 1 + s))
            dp[(r, c, k2)] = s
        return -1