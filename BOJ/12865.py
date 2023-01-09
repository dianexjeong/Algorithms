import sys

n, k = map(int, sys.stdin.readline().split())
items = [[0, 0]]
knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for _ in range(n):
    items.append(list(map(int, sys.stdin.readline().split())))


for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = items[i][0]
        price = items[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(
                price + knapsack[i - 1][j - weight], knapsack[i - 1][j]
            )

print(knapsack[n][k])
