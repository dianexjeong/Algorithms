import sys
sum=10

arr=[0]*10
for i in range(10):
    n=int(sys.stdin.readline())
    arr[i]=n%42

arr=set(arr)
print(len(arr))
    
    