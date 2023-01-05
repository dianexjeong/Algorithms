import sys
from collections import deque

n = int(sys.stdin.readline())
housing = []
housinglist = []

for i in range(n):
    housing.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
housingfinalcount = 0


def bfs():
    count = 0
    housingcount = 0
    for a in range(n):
        for b in range(n):
            x = a
            y = b
            if housing[x][y] == 1:
                housingcount += 1
                housing[x][y] = 0
                count += 1
                queue = deque()
                queue.append((x, y))
                while queue:
                    x, y = queue.popleft()

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if (0 <= nx < n) and (0 <= ny < n) and (housing[nx][ny] == 1):
                            housingcount += 1
                            queue.append((nx, ny))
                            housing[nx][ny] = 0
                housinglist.append(housingcount)
                housingcount = 0
    return count


housingfinalcount = bfs()
housinglist.sort()
print(housingfinalcount)
for i in housinglist:
    print(i)
