num=int(input())
for i in range(num):
    count, s=(input().split())
    text=''
    for j in s:
        text+=int(count)*j
    print(text)

