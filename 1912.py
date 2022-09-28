import sys
n=int(sys.stdin.readline())
flag=0
arr=[]

def kadane(a):
    maxall=a[0]; maxhere=0
    for i in a:
        if ((maxhere+i)<0):
            maxhere=0
        else:
            maxhere+=i
        if (maxhere>maxall):
            maxall=maxhere
    return maxall

      
arr=list(map(int, sys.stdin.readline().split()))
if (max(arr)<=0):
    print(max(arr))

else:
    max=kadane(arr)
    print(max)