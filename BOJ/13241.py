import sys

a, b = map(int, sys.stdin.readline().split())

mul = a * b

while b:
    if a > b:
        a, b = b, a
    b %= a


print(mul // a)
