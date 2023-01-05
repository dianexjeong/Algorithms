import sys
n=int(sys.stdin.readline())
base=list(map(int,sys.stdin.readline().split()))
base.sort()
m=int(sys.stdin.readline())
find=list(map(int,sys.stdin.readline().split()))

# binary는 반드시 정렬된 상태에서 시작해야 함!
def binary(a):
    low=0; high=n-1; mid=0
    while(low<=high):
        mid=(low+high)//2
        if(base[mid]<a):
            low=mid+1
        elif(base[mid]>a):
            high=mid-1
        else:
            return 1
    return 0


for i in range(m):
    print(binary(find[i]))
