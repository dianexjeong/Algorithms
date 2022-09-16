k=int(input())
stack=[]; sum=0
for i in range(k):
    new=int(input())
    if (new==0):
        stack.pop()
    else:
        stack.append(new)

for j in stack:
        sum+=j
print(sum)
