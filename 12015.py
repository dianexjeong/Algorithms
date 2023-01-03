import sys

n = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))

memo = [numlist[0]]


def lis(item):  # binary insertion
    start = 0
    end = len(memo) - 1

    while start <= end:
        mid = (start + end) // 2

        if memo[mid] == item:
            return mid
        elif memo[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
    return start


for i in range(1, len(numlist)):
    if memo[-1] >= numlist[i]:
        idx = lis(numlist[i])
        memo[idx] = numlist[i]
    else:
        memo.append(numlist[i])

print(len(memo))
