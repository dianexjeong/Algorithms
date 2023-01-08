import sys

avg = 0

for _ in range(5):
    tmp = int(sys.stdin.readline())
    if tmp < 40:
        tmp = 40
    avg += tmp

print(avg // 5)
