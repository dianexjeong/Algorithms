import sys

word = sys.stdin.readline().strip()

abc = [-1 for _ in range(26)]

for i in range(len(word)):
    if abc[ord(word[i]) - 97] >= 0:
        continue
    abc[ord(word[i]) - 97] = i

for i in range(26):
    print(abc[i], end=" ")
