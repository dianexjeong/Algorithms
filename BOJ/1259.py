while(True):
    num=(input())
    if(num=='0'):
        break
    front=num
    back=num[::-1]
    
    if(front==back):
        print('yes')
    else:
        print('no')
