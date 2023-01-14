import sys

numlist=list(map(int, sys.stdin.readline().split()))

numlist.sort()

for i in numlist:
    print(i, end=" ")