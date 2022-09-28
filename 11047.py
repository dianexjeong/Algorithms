import sys
n, cost=map(int, sys.stdin.readline().split())
types=[]; count=0
for i in range(n):
    types.append(int(sys.stdin.readline()))
types.sort(reverse=True)
for i in (types):
    if cost>=i:
        count+=cost//i
        cost%=i
        if (cost<=0):
            break
print(count)
            