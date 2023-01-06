import sys

n = int(sys.stdin.readline())
housing = []

for _ in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    house = [r, g, b]
    housing.append(house)

for i in range(1, n):
    housing[i][0] = min(housing[i - 1][1], housing[i - 1][2]) + housing[i][0]
    housing[i][1] = min(housing[i - 1][0], housing[i - 1][2]) + housing[i][1]
    housing[i][2] = min(housing[i - 1][0], housing[i - 1][1]) + housing[i][2]

print(min(housing[n - 1]))
