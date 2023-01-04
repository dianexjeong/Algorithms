import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    a = int(str(a)[-1])
    two = b % 2
    four = b % 4
    if two == 0:
        two = 2
    if four == 0:
        four = 4
    if a == 0:
        print(10)
    elif a == 1:
        print(1)
    elif a == 2:
        idx = [0, 2, 4, 8, 6]
        print(idx[four])
    elif a == 3:
        idx = [0, 3, 9, 7, 1]
        print(idx[four])
    elif a == 4:
        idx = [0, 4, 6]
        print(idx[two])
    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a == 7:
        idx = [0, 7, 9, 3, 1]
        print(idx[four])
    elif a == 8:
        idx = [0, 8, 4, 2, 6]
        print(idx[four])
    elif a == 9:
        idx = [0, 9, 1]
        print(idx[two])
