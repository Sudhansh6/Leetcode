class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited = [0] * n
        vi = 0
        cv = 0
        res = 0

        adj = [list() for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque()
        for i in range(n):
            if visited[i]:
                continue

            q.appendleft(i)
            visited[i] = 1
            while(q):
                u = q.pop()
                vi += 1
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = 1
                        q.appendleft(v)
            cv += vi
            res += (n - cv)*vi
            vi = 0
        return res