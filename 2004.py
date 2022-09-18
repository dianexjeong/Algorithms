import sys
n, k=map(int, sys.stdin.readline().split())

def num(a, b):
    count=0
    while (a!=0):
        a=a//b
        count+=a
    return count
if (k==0): print(0)
else:
    print(min((num(n, 5)-num(n-k, 5)-num(k, 5)), (num(n, 2)-num(n-k, 2)-num(k, 2))))