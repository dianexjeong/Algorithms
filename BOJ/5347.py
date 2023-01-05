import sys
n=int(sys.stdin.readline())
for i in range(n):
    a, b=map(int, sys.stdin.readline().split())
    mul=a*b
    while(b>0):
        a, b=b, a%b
    print(mul//a)

