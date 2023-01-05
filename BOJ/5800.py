n=int(input())
for i in range(n):
    gap=0
    score=list(map(int, input().split()))
    del score[0]
    score.sort()
    for j in range(len(score)-1):
        temp=abs(score[j+1]-score[j])
        if (temp>gap):
            gap=temp
    print("Class", i+1)
    print("Max "+str(max(score))+", Min "+str(min(score))+", Largest gap "+str(gap))