import sys
n=int(sys.stdin.readline())
e=dict()

for i in range(n):
    name, cmd=sys.stdin.readline().split()
    if (cmd=='enter'):
        e[name]=1
    else:
        del e[name]

e=sorted(e.keys(), reverse=True)

for k in e:
    print(k)
