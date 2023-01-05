import sys

def find(parent, a):
    if parent[a]==-1:
        return a
    else:
        parent[a]=find(parent, parent[a])
        return parent[a]

def unionfind(parent, a, b):
    rootA=find(parent, a)
    rootB=find(parent, b)
    if (rootA>rootB):
        parent[rootA]=rootB
    else:
        parent[rootB]=rootA
    return

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[0,0,0]]; parent=[-1]*(n+1)
result=0
for _ in range(m):
    a, b, c=map(int, sys.stdin.readline().split())
    graph.append([c, a, b])
graph.sort()

for edge in graph:
    cost, a, b=edge
    if((find(parent, a)!=find(parent, b))):
        unionfind(parent, a, b)
        result+=cost
print(result)
