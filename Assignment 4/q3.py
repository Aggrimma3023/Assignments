print("welcome to the multiplication game")
import random
count=0
while count<11:
    a=(random.randint(0,10))
    b=(random.randint(0,10))
    print("Find product of numbers",a,b)
    prod=int(input())
    if prod==a*b:
        print("Right!")
    else:print("wrong")
    count=count+1
print("game finished")



