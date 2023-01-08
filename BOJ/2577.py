import sys

mul = 1
numlist = [0 for _ in range(10)]

for _ in range(3):
    tmp = int(sys.stdin.readline())
    mul *= tmp

mul = str(mul)

for i in mul:
    numlist[int(i)] += 1

for a in numlist:
    print(a)
