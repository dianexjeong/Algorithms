import sys

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

numlist = [i for i in range(n + 1)]
arr = []


def dfs():
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n + 1):
        arr.append(i)
        dfs()
        arr.pop()


dfs()
