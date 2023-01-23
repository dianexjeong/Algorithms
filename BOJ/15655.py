import sys

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

tmplist = list(map(int, sys.stdin.readline().split()))
tmplist.sort()

numlist = []

for i in range(n):
    numlist.append([tmplist[i], False])

arr = []


def dfs():
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(n):
        if not numlist[i][1]:
            if len(arr) >= 1:
                if numlist[i][0] > arr[len(arr) - 1]:
                    numlist[i][1] = True
                    arr.append(numlist[i][0])
                    dfs()
                    numlist[i][1] = False
                    arr.pop()
                continue
            numlist[i][1] = True
            arr.append(numlist[i][0])
            dfs()
            numlist[i][1] = False
            arr.pop()


dfs()
