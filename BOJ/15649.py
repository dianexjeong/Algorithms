import sys

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

numlist = [i for i in range(n + 1)]
visited = [False] * (n + 1)
arr = []


def dfs():
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            if len(arr) >= 1:
                if i > arr[len(arr) - 1]:
                    visited[i] = True
                    arr.append(i)
                    dfs()
                    visited[i] = False
                    arr.pop()
                continue
            visited[i] = True
            arr.append(i)
            dfs()
            visited[i] = False
            arr.pop()


dfs()
