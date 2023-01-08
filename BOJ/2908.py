import sys

a, b = map(int, sys.stdin.readline().split())

a = str(a)[::-1]
b = str(b)[::-1]

print(int(a) if int(a) > int(b) else int(b))
