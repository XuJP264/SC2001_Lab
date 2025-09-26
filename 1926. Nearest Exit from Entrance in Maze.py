class Solution:
    def __init__(self):
        self.width = 0
        self.length = 0

    def border(self, cor):
        return cor[0] in [0, self.length - 1] or cor[1] in [0, self.width - 1]

    def isLegal(self, maze, cor, move, q, visited, step):
        x, y = cor[0], cor[1]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        dx, dy = directions[move]
        nx, ny = x + dx, y + dy
        if 0 <= nx < self.length and 0 <= ny < self.width and maze[nx][ny] == '.':
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append([[nx, ny], step + 1, move])

    def nearestExit(self, maze, entrance):
        q = []
        visits = set()
        tail = 0
        self.length = len(maze)
        self.width = len(maze[0])

        ex, ey = entrance
        q.append([[ex, ey], 0, -999])
        visits.add((ex, ey))

        while tail < len(q):
            cur = q[tail]
            tail += 1
            x, y = cur[0]
            if self.border([x, y]) and [x, y] != entrance:
                return cur[1]
            for i in range(4):
                if cur[2] + i == 1 or cur[2] + i == 5:
                    continue
                self.isLegal(maze, [x, y], i, q, visits, cur[1])
        return -1
