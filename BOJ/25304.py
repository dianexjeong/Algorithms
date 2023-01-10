import sys

total=int(sys.stdin.readline())
n=int(sys.stdin.readline())

sum=0
for _ in range(n):
    item, cnt=map(int, sys.stdin.readline().split())
    sum+=item*cnt

if sum==total:
    print("Yes")
else:
    print("No")