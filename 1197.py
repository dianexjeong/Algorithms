import sys
v, e=map(int, sys.stdin.readline().split())
parent=[-1]*(v+1); arr=[]
result=0

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

for i in range(e):
    a, b, c=map(int, sys.stdin.readline().split())
    arr.append([c, a, b])

arr.sort()

for edge in arr:
    cost, a, b=edge
    if ((find(parent, a)!=find(parent, b))):
        unionfind(parent, a, b)
        result+=cost
        
print(result)

