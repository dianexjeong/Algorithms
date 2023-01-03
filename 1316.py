import sys

groupCnt = 0
n = int(sys.stdin.readline())
for _ in range(n):
    count = [0 for _ in range(26)]
    word = sys.stdin.readline().strip()
    if len(word) == 1:
        groupCnt += 1
        continue
    count[ord(word[0]) - 97] = 1
    for i in range(1, len(word)):
        if word[i - 1] != word[i]:
            if count[ord(word[i]) - 97] != 0:
                break
            count[ord(word[i]) - 97] = 1
        if i == len(word) - 1:
            groupCnt += 1

print(groupCnt)
