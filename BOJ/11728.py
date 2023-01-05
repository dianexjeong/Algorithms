import sys
n, m=map(int, sys.stdin.readline().split())
arr1=list(map(int, sys.stdin.readline().split()))
arr2=list(map(int, sys.stdin.readline().split()))
arr1.sort()
arr2.sort()
sortedarr=[]
i=j=0
while (i<n and j<m):
    if (arr1[i]<=arr2[j]):
        sortedarr.append(arr1[i])
        i+=1
    else:
        sortedarr.append(arr2[j])
        j+=1
while (i<n):
    sortedarr.append(arr1[i])
    i+=1   
while (j<m):
    sortedarr.append(arr2[j])
    j+=1

for i in range(len(sortedarr)):
    print(sortedarr[i], end='')
    print(' ', end='')
