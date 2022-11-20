import sys
testcase=int(sys.stdin.readline())
for i in range(testcase):
    flag=0
    totalfunc=str(sys.stdin.readline().strip())
    func=list(totalfunc)
    n=int(sys.stdin.readline())
    end=n-1
    err=0
    if n!=0: 
        arr=sys.stdin.readline().rstrip()[1:-1].split(",")
        arr=list(map(int, arr))
    elif n==0: 
        tmp=sys.stdin.readline().strip()
        arr=[]

    for j in func:
        if j=='R':
            if flag==0:
                flag=1
            else:
                flag=0
        elif j=='D':
            if (end<0):
                print('error')
                err=1
                break
            elif flag==0:
                del(arr[0])
            elif flag==1:
                del(arr[end])
            end-=1
 
    if flag==1:
        if err==0: print('[', end='')
        rev=list(reversed(arr))
        for m in range(len(rev)):
            print(rev[m], end='')
            if m!=len(rev)-1:
                print(',', end='')
        if err==0: print(']')
            
    else:
        if err==0: print('[', end='')
        for m in range(len(arr)):
            print(arr[m], end='')
            if m!=len(arr)-1:
                print(',', end='')
        if err==0: print(']')
