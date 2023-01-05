import sys
n=sys.stdin.readline().strip()
abc=[0]*26; 
n=n.upper()
for i in range(len(n)):
    for j in range(65, 65+27):
        if (chr(j)==n[i]):
            abc[j-65]+=1


if(abc.count(max(abc))>1):
    print("?")
else:
    print(chr(abc.index(max(abc))+65))