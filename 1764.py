import sys
n, m=map(int, sys.stdin.readline().split())
nset=set(); mset=set()
for i in range(n):
    nset.add(str(sys.stdin.readline().strip()))
for i in range(m):
    mset.add(str(sys.stdin.readline().strip()))
intersection=sorted(list(nset&mset))
print(len(intersection))
for i in intersection:
    print(i)