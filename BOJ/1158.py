import sys
n, k=map(int, sys.stdin.readline().split())
arr=[i for i in range(1, n+1)]
ans=[]; idx=0

for i in range(n):
    idx+=k-1
    if (idx>=len(arr)):
        idx%=len(arr)
    ans.append(str(arr.pop(idx)))
print("<",", ".join(ans)[:],">", sep='')