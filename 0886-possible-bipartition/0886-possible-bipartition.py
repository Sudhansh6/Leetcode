class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [0] * (n + 1)  # 0 = uncolored, 1 = first group, -1 = second group
        adj = [[] for _ in range(n + 1)]

        # Build adjacency list
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)  # Ensure bidirectional connection

        # BFS on unvisited components
        for i in range(1, n + 1):
            if colors[i] == 0:  # Start BFS if unvisited
                q = deque([i])
                colors[i] = 1  # Assign first group

                while q:
                    u = q.popleft()
                    for v in adj[u]:
                        if colors[v] == 0:  # If uncolored, assign opposite color
                            colors[v] = -colors[u]
                            q.append(v)
                        elif colors[v] == colors[u]:  # Conflict found
                            return False

        return True
