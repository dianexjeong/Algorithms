import sys
n=int(sys.stdin.readline())
arr=[0]*(10001)
for i in range(n):
    k=int(sys.stdin.readline())
    arr[k]+=1

for i in range(1, 10001):
    while arr[i]!=0:
        print(i); arr[i]-=1