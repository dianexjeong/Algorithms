import sys

def dfs(a, arr):
    arr[a]=-2
    for i in range(len(arr)):
        if a==arr[i]:
            dfs(i, arr)
    return

n=int(sys.stdin.readline())
parent=list(map(int, sys.stdin.readline().split()))
delete=int(sys.stdin.readline())
dfs(delete, parent)

count=0
for i in range(n):
    if ((parent[i]!=-2) and (i not in parent)):
        count+=1
print(count)


    