n=int(input())
inc=[]
for i in range(n):
    inc.append(int(input()))

sort=sorted(inc)

for j in range(n):
    print(sort[j])
