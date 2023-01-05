import sys
t=int(sys.stdin.readline())
for j in range(t):
    n=int(sys.stdin.readline())
    tri=[0,1,1,1,2,2,3,4,5,7,9]
    if (n>10):
        for i in range(11, n+1):
            tri.append(tri[i-5]+tri[i-1])
    print(tri[n])