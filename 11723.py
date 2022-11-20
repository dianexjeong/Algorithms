import sys
S=set()
n=int(sys.stdin.readline())
for i in range(n):
    tmp=sys.stdin.readline().strip().split()
    if len(tmp)==1:
        if tmp[0]=='all':
            S=set([i for i in range(1, 21)])
        else: S=set()
    else:
        x=int(tmp[1])
        if tmp[0]=='add':
            S.add(x)
        elif tmp[0]=='remove':
            S.discard(x)
        elif tmp[0]=='check':
            if x in S:
                print(1)
            else: print(0)
        elif tmp[0]=='toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)