n=int(input())
for i in range(n):
    score=0; count=0
    test=input()
    for j in test:
        if (j=='O'):
            count+=1
            score+=count
        elif (j=='X'):
            count=0
    print(score)
