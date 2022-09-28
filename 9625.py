import sys
n=int(sys.stdin.readline())
numAB=[[1,0],[0,1],[1,1]]
for i in range(3, n+1):
    numAB.append([numAB[i-1][1], numAB[i-1][0]+numAB[i-1][1]])
print(numAB[n][0], numAB[n][1])