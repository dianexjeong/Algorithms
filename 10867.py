import sys
n=int(sys.stdin.readline())
l=list(map(int, sys.stdin.readline().split()))
l=set(l); l=list(l)
l.sort()
for i in l:
    print(int(i), end=' ')