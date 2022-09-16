n=int(input())
lvl=1; lbound=1

while(n>lbound):
    lbound+=6*lvl
    lvl+=1

print(lvl)
