import sys

n = int(sys.stdin.readline())

firstnum = int(sys.stdin.readline())
tmplist = []
listmax = 0
for i in range(n - 1):
    newlist = list(map(int, sys.stdin.readline().split()))

    if i == 0:
        for j in range(2):
            newlist[j] += firstnum
        tmplist = newlist[:]

    else:
        for j in range(len(tmplist)):
            if j == 0:
                newlist[0] += tmplist[0]
            elif j == len(tmplist) - 1:
                newlist[-1] += tmplist[-1]
            else:
                newlist[j] += max(tmplist[j - 1], tmplist[j])
        tmplist = []
        tmplist = newlist[:]

if n == 1:
    print(firstnum)
else:
    print(max(tmplist))
