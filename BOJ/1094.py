import sys

wood=[64, 32, 16, 8, 4, 2, 1]

x=int(sys.stdin.readline())
count=0

for i in wood:
    if i>x: continue
    x-=i
    count+=1
    
print(count)
    