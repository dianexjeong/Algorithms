import sys
n=str(sys.stdin.readline().strip())
l=list(n)

for i in l:
    i=int(i)

l.sort(reverse=True)
l=''.join(l); l=int(l)
print(l)