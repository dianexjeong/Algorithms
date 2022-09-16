text=input()
happy=text.count(":-)")
sad=text.count(":-(")

if((happy==0)&(sad==0)):
    print("none")
elif(happy>sad):
    print("happy")
elif(sad>happy):
    print("sad")
elif(happy==sad):
    print("unsure")