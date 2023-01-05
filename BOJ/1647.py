import sys
n, m=map(int, sys.stdin.readline().split())
parent=[-1]*(n+1); graph=[]; result=0
def find(parent, a):
    if parent[a]==-1:
        return a
    else:
        parent[a]=find(parent, parent[a])
        return parent[a]
    
def unionfind(parent, a, b):
    rootA=find(parent, a)
    rootB=find(parent, b)
    if rootA>rootB:
        parent[rootA]=rootB
    else:
        parent[rootB]=rootA
    return

for _ in range(m):
    a, b, c=map(int, sys.stdin.readline().split())
    graph.append([c, a, b])
graph.sort()
newgraph=[]
for edge in graph:
    cost, a, b=edge
    if (find(parent, a)!=find(parent, b)):
        unionfind(parent, a, b)
        newgraph.append(edge)
        result+=cost
newgraph.sort()
result-=newgraph[-1][0]
print(result)
        
