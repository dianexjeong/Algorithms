import sys
from collections import deque

def dfs(n):
    visited[n]=True
    print(n, end=' ')
    for i in graph[n]:
        if not visited[i]:
            dfs(i)
    return

def bfs(n):
    q=deque()
    q.append(n)
    visited[n]=True
    while q:
        i=q.popleft()
        print(i, end=' ')
        for j in graph[i]:
            if not visited[j]:
                q.append(j)
                visited[j]=True
    return

n, m, search=map(int, sys.stdin.readline().split())
graph=[[] for _ in range (1+n)]
for i in range(m):
    r, l=map(int, sys.stdin.readline().split())
    graph[r].append(l)
    graph[l].append(r)
for i in range(1, n+1):
    graph[i].sort()
    
visited=[False]*(n+1)
dfs(search)
visited=[False]*(n+1)
print(); bfs(search)

