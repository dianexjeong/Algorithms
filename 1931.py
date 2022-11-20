import sys
n=int(sys.stdin.readline())
meeting=[]
for _ in range(n):
    start, end=map(int, sys.stdin.readline().split())
    duration=end-start
    meeting.append([start, end])
meeting=sorted(meeting, key=lambda a: a[0])
meeting=sorted(meeting, key=lambda a: a[1])
last=0; count=0

for i, j in meeting:
    if i>=last:
        count+=1
        last=j

print(count)