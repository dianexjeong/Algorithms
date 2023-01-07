import sys

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

numlist = [i for i in range(n + 1)]
visited = [False] * (n + 1)
arr = []


def dfs():
    if len(arr) == m:
        for j in range(2, len(arr) + 1):
            if arr[j] < arr[j - 1]:
                break
            if j == len(arr):
                print(" ".join(map(str, arr)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs()
            visited[i] = False
            arr.pop()


dfs()
