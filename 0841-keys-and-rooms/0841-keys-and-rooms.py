class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]*len(rooms)
        num = 1
        q = deque([0])
        visited[0] = 1

        while len(q):
            u = q.pop()

            for v in rooms[u]:
                if visited[v]:
                    continue
                visited[v] = 1
                num += 1
                q.appendleft(v)
                
        return num == len(rooms)
            
