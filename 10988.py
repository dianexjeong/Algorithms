s=input()
flag=1
for i in range(len(s)):
    if (s[i]!=s[len(s)-1-i]):
        flag=0
        break
print(flag)
