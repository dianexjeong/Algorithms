# merge sort
import sys, math
n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
        
def mergesort(A):
    if len(A)<2: return A
    q=len(A)//2
    lowarr=mergesort(A[:q])
    higharr=mergesort(A[q:])
    mergedarr=[]
    i=j=0
    while(i<len(lowarr) and j<len(higharr)):
        if lowarr[i]<=higharr[j]:
            mergedarr.append(lowarr[i])
            i+=1
        else:
            mergedarr.append(higharr[j])
            j+=1
    mergedarr+=lowarr[i:]
    mergedarr+=higharr[j:]
    return mergedarr
    
time=mergesort(time)
for i in range(1, n):
    time[i]+=time[i-1]
sum=0
for i in range(n):
    sum+=time[i]
    
print(sum)