import sys
n=int(sys.stdin.readline())
n=1000-n
count=0

while(n>0):
    if (n>=500):
        div=500
    elif (n>=100):
        div=100
    elif (n>=50):
        div=50
    elif (n>=10):
        div=10
    elif (n>=5):
        div=5
    else: div=1
    
    new=n%div
    count+=n//div
    n=new

print(count)
        