import sys
i=int(sys.stdin.readline())
n=sys.stdin.readline().strip()
sum=0

for j in n:
    sum+=int(j)
print(sum)
