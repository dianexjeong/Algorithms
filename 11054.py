import sys

n = int(sys.stdin.readline())

numlist = list(map(int, sys.stdin.readline().split()))
revlist = numlist[::-1]

increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if numlist[i] > numlist[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if revlist[i] > revlist[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = increase[i] + decrease[n - i - 1] - 1
print(max(result))
