x, y, w, h=map(int, input().split())

dif1=min(x, (w-x))
dif2=min(y, (h-y))
print(min(dif1, dif2))