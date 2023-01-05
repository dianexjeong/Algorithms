import sys
n=int(sys.stdin.readline())
arr=[]; count=0
for i in range(n):
    age, name=sys.stdin.readline().split()
    age=int(age)
    name=name.strip()
    count+=1
    arr.append([age, name])

arr.sort(key=lambda x:x[0])

for i in range(len(arr)):
    print(arr[i][0], arr[i][1])