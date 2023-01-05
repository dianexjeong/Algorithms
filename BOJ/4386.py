import sys, math

# root가 같은지를 찾아가는 것
def find(parent, a):
    if parent[a]==a:
        return a
    else: 
        parent[a]=find(parent, parent[a])
        return parent[a]

# 새로운 edge에 대해서 root를 합쳐서 '연결' 하는 것
def unionfind(parent, a, b):
    rootA=find(parent, a)
    rootB=find(parent, b)
    if (rootA>rootB):
        parent[rootA]=rootB
    else:
        parent[rootB]=rootA
    return

def kruskal(n):
    return

n=int(sys.stdin.readline())
stars=[]
graph=[]
parent=[i for i in range(n)]
    
for _ in range(n):
    x, y=map(float, sys.stdin.readline().split())
    stars.append([x, y])

for i in range(n):
    x1, y1=stars[i][0], stars[i][1]
    for j in range(i+1, n):
        x2, y2=stars[j][0], stars[j][1]
        dist=math.sqrt((x1-x2)**2+(y1-y2)**2)
        dist=round(dist,2)
        graph.append([dist, i, j])
graph.sort()
result=0
for edge in graph:
    cost, a, b=edge #이미 edge에 세개의 항목 있으니까 순서대로 이름 부여
    if(find(parent, a) != find(parent, b)):
        unionfind(parent, a, b)
        result+=cost
        
print(result)
    
        
    
    
    

        
