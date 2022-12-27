import sys

start=0
flag=0
br=0
n=int(sys.stdin.readline())
for _ in range(n):
    flag=0
    start=0
    par=sys.stdin.readline().strip()
    for i in range(len(par)):
        if par[i]=="(":
            flag+=1
            start=1
        else: 
            flag-=1
            start=1
        if (flag<0):
            print("NO")
            br=1
            break
    if (br==1):
        br=0
        continue
    if (flag!=0):
        print("NO")
    else:
        print("YES")
        