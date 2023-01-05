import sys
n, m=map(int, sys.stdin.readline().split())
sumtable=[[0]*(n+1)]
for i in range(n):
    row=[0]+list(map(int, sys.stdin.readline().split()))
    sumtable.append(row)
    
# prefix sum 만들기
# 행 더하기
for i in range(1,n+1):
    for j in range(1,n+1):
        sumtable[i][j]+=sumtable[i-1][j]
# 열 더하기
for j in range(1,n+1):
    for i in range(1,n+1):
        sumtable[i][j]+=sumtable[i][j-1]
        
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sum=sumtable[x2][y2]-sumtable[x1-1][y2]-sumtable[x2][y1-1]+sumtable[x1-1][y1-1]
    print(sum)
