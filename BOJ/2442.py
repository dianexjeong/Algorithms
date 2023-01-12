import sys

n=int(sys.stdin.readline())

for i in range(n-1, -1, -1):
    for j in range(i):
        print(" ", end="")
    for k in range(1, 2*(n-i)):
        print("*", end="")
    print()