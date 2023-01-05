import sys, math
up, down, m=map(int, sys.stdin.readline().split())
m-=up; f=up-down; cnt=1
cnt+=(m//f)
if ((m%f)>0):
    cnt+=1
print(cnt)