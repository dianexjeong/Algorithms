import sys
n, d=map(int, sys.stdin.readline().split())
count=0
for i in range(1, n+1):
    count+=str(i).count(str(d))
print(count)