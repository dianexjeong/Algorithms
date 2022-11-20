import sys
num=list(map(int, sys.stdin.readline().split()))
for i in range(1, 3):
    key=num[i]
    j=i-1
    while(num[j]>=key and j>=0):
        num[j+1]=num[j]
        j-=1
    num[j+1]=key
    
print(num[1])
    