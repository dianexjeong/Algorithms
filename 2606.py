def dfs(n):
    visited[n]=True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)
    
import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()
    
visited=[False]*(n+1)
dfs(1)
print(visited.count(True)-1)

