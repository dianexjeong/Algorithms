import sys

word = sys.stdin.readline().strip()

abc = [0 for _ in range(26)]

for i in range(len(word)):
    abc[ord(word[i]) - 97] += 1

for i in range(26):
    print(abc[i], end=" ")
