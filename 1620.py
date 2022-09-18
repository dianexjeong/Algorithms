import sys
a, b=map(int, sys.stdin.readline().split())

ency={} # num : pokemon
encyswap={} # pokemon : num

for i in range(a):
    pokemon=sys.stdin.readline().strip()
    ency[str(i+1)]=pokemon

encyswap= {v:k for k, v in ency.items()}

for j in range(b):
    find=sys.stdin.readline().strip()
    if (ord(find[0])>=65):
        print(encyswap[find])
    else:
        print(ency[find])