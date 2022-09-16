import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    x, y=map(int, sys.stdin.readline().split())
    arr.append([x, y])

arr.sort(key=lambda a: a[1])
arr.sort(key=lambda b: b[0])

for j in range(n):
    print(arr[j][0], arr[j][1])