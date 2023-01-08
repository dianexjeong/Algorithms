import sys

n = int(sys.stdin.readline())

for i in range(n):
    for j in range(i):
        print(" ", end="")
    for _ in range(n - i):
        print("*", end="")
    print("\n", end="")
