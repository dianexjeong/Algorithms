import sys

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

numlist = [0] + list(map(int, sys.stdin.readline().split()))
numlist.sort()
visited = [False] * (n + 1)
arr = []


def dfs():
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(numlist[i])
            dfs()
            visited[i] = False
            arr.pop()


dfs()
