class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dd = [1, 0, -1, 0, 1]
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        while len(q):  
            r, c, d = q.pop()

            for i in range(4):
                nr, nc = r + dd[i], c + dd[i + 1]

                if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
                    if maze[nr][nc] == '+':
                        continue
                    if nr == 0 or nr == len(maze) - 1 or nc == 0 or nc == len(maze[0]) - 1:
                        return d + 1     
                    maze[nr][nc] = '+'   
                    q.appendleft((nr, nc, d + 1))
        return -1