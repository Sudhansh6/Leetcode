class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # Find friends of friends until the level using BFS
        q = deque([(id, 0)])
        req_l = []
        visited = [0] * len(friends)
        visited[id] = 1
        
        while len(q):
            u, l = q.pop()
            if l == level:
                req_l.append(u)
                continue 
            
            # visited[u] = 1
            for v in friends[u]:
                if not visited[v]:
                    visited[v] = 1
                    q.appendleft((v, l + 1))

        res = {}
        for u in req_l:
            for m in watchedVideos[u]:
                res[m] = res.get(m, 0) + 1 
        return [k for k, v in sorted(res.items(), key = lambda x: (x[1], x[0]))]
        