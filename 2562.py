index=0; temp=0; max=0; maxindex=0
for i in range (9):
    temp=int(input())
    index+=1

    if temp>max:
        max=temp
        maxindex=index

print(max)
print(maxindex)