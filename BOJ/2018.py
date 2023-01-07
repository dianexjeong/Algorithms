import sys

n = int(sys.stdin.readline())

start, end, count, total = 1, 1, 0, 1

while end != n:
    if total < n:
        end += 1
        total += end
    elif total > n:
        total -= start
        start += 1
    else:
        count += 1
        end += 1
        total += end

print(count + 1)
