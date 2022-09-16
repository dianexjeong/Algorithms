arr=[]
import sys
a=int(sys.stdin.readline())

def push(n):
    arr.append(n)

def pop():
    if (len(arr)==0):
        print('-1')
    else:
        n=arr[0]
        del arr[0]
        print(n)
   
def size():
    print(len(arr))

def empty():
    if (len(arr)==0):
        print('1')
    else:
        print('0')

def front():
    if (len(arr)==0):
        print('-1')
    else:
        print(arr[0])

def back():
    if (len(arr)==0):
        print('-1')
    else:
        print(arr[-1])

for i in range(a):
    input=sys.stdin.readline().split()
    cmd=input[0]
    if (cmd=='push'):
        push(input[1])
    elif (cmd=='pop'):
        pop()
    elif (cmd=='size'):
        size()
    elif (cmd=='empty'):
        empty()
    elif (cmd=='front'):
        front()
    elif (cmd=='back'):
        back()