import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = []
dist = [[1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    maze.append(list(map(int, sys.stdin.readline().strip())))

distance = [[1 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        if (x == n - 1) and (y == m - 1):
            return distance[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                (0 <= nx < n)
                and (0 <= ny < m)
                and (maze[nx][ny] == 1)
                and (distance[nx][ny] == 1)
            ):
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1


print(bfs(0, 0))
