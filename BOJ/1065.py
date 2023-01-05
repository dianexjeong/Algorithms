import sys

n = int(sys.stdin.readline())
count = 0
if n < 100:
    print(n)
elif n < 111:
    print(99)
else:
    if n >= 111:
        for j in range(111, n + 1):
            nstr = str(j)
            nlist = []
            for i in nstr:
                nlist.append(int(i))
            if (nlist[0] - nlist[1]) == (nlist[1] - nlist[2]):
                count += 1
    print(count + 99)
