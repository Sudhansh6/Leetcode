class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0]*len(isConnected)
        res = 0
        for i in range(len(visited)):
            if not visited[i]:
                q = deque([i])

                while len(q):
                    u = q.pop()

                    for j in range(len(visited)):
                        if visited[j]:
                            continue
                        if isConnected[i][j]:
                            visited[j] = 1
                            q.appendleft(j)
                
                res += 1
        return res