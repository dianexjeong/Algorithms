import sys

n, k = map(int, sys.stdin.readline().split())
numlist = list(map(int, sys.stdin.readline().split()))
numlist.sort()
print(numlist[k - 1])
