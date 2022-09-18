import sys
a, b=map(int, sys.stdin.readline().split())

dic={}

for i in range(a):
    web, pw=sys.stdin.readline().split()
    dic[web]=pw
    
for i in range(b):
    search=sys.stdin.readline().strip()
    print(dic[search])