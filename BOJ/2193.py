import sys, math
n=int(sys.stdin.readline())

fac=[1,1,2]
for i in range(3, n+1):
    fac.append(fac[i-1]*i)
    
def comb(n, k):
    return ((fac[n]//(fac[n-k]*fac[k])))

val=0; rest=n-2; imax=math.ceil(rest/2)
pn=[0,1,1,2,3]

for i in range(imax+1):
    if (i==0): val+=1
    else:
        nn=rest+1-i
        inum=comb((rest+1-i),i)
        val+=inum
if (n<=4):
    print(pn[n])  
else:      
    print(val)
        
