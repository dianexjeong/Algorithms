import sys
import heapq

n=int(sys.stdin.readline())

for _ in range(n):
    result=0
    k=int(sys.stdin.readline())
    arr=list(map(int, sys.stdin.readline().split()))
    heapq.heapify(arr)
    
    while (len(arr)>1):
        a=heapq.heappop(arr)
        b=heapq.heappop(arr)
        result+=(a+b)
        heapq.heappush(arr, (a+b))
    print(result)