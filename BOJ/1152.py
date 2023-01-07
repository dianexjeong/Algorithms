import sys

sentence = sys.stdin.readline().strip()
sum = 0
flag = -1
for i in range(len(sentence)):
    flag = 0
    if sentence[i] == " ":
        if i == 0 or i == len(sentence) - 1:
            flag = 1
            continue
        sum += 1

if sum == 0 and flag == 1:
    print(0)
elif flag != -1:
    print(sum + 1)
else:
    print(0)
