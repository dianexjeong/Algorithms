import sys
i=int(sys.stdin.readline())
word=[]
for n in range(i):
    word.append(sys.stdin.readline().strip())
word=list(set(word))

word.sort()
word.sort(key=len)

for j in range(len(word)):
    print(word[j])
