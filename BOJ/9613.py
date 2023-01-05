import sys
import math
t=int(sys.stdin.readline())
for i in range(t):
    arr=list(map(int, sys.stdin.readline().split()))
    n=arr[0]; del(arr[0]); sum=0
    for j in range(n):
        for k in range(j+1, n):
            sum+=math.gcd(arr[j], arr[k])
    print(sum)