import sys
x=str(sys.stdin.readline().strip())
l=list(x)
cnt=0
new=0
if (len(l)==1):
    print(cnt)
    if (int(x)%3==0):
        print('YES')
    else:
        print('NO')
else:
    while(len(l)!=1):
        new=0
        for i in l:
            i=int(i); new+=i
        new=str(new)
        l=list(new)
        cnt+=1

    print(cnt)
    if (int(new)%3==0):
        print('YES')
    else:
        print('NO')
    
        
    
