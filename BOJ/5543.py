import sys

burger = []
coke = 0
sprite = 0

for _ in range(3):
    tmp = int(sys.stdin.readline())
    burger.append(tmp)
coke = int(sys.stdin.readline())
sprite = int(sys.stdin.readline())

print(min(burger) + (sprite if coke > sprite else coke) - 50)
