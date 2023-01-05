import sys
n, m=map(int, sys.stdin.readline().split())
arr=list(map(int, sys.stdin.readline().split()))
sumarr=[0]
for i in range(1,n+1):
    sumarr.append(sumarr[i-1]+arr[i-1])
for i in range(m):
    a, b=map(int, sys.stdin.readline().split())
    print(sumarr[b]-sumarr[a-1])
