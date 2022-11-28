import sys
string=list(sys.stdin.readline().strip())
count=0

for i in range(1,len(string)):
    if (string[i]!=string[i-1]):
        count+=1

if (count==1):
    print(count)
else: print((count+1)//2)
