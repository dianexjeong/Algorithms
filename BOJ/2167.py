import sys
n, m=map(int, sys.stdin.readline().split())
arr=[[0 for _ in range(m+1)]]

for i in range(n):
    row=list(map(int, sys.stdin.readline().split()))
    row.insert(0, 0)
    arr.append(row)

k=int(sys.stdin.readline())

for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i][j]+=arr[i][j-1]

for j in range(1, m+1):
    for i in range(1, n+1):
        arr[i][j]+=arr[i-1][j]

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sum=0
    sum+=arr[x2][y2]-arr[x1-1][y2]-arr[x2][y1-1]+arr[x1-1][y1-1]
    print(sum)


