m=int(input())
n=int(input())
flag=0; sum=0; min=0
for i in range(m, n+1):
    if(i==2):
        min=2; sum+=2; flag=1
        continue
    for j in range(2, i):
        if(i%j==0):
            break
        elif(j==i-1):
            if(flag==0):
                flag=1; sum+=i; min=i
            else:
                sum+=i
if(sum==0):
    print("-1")
else:
    print(sum)
    print(min)
    

