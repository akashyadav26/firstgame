import random
name=input("welcome tell your name:  ")
print(f"Hi {name}")
print("THIS IS A NUMBER GESSING GAME")
number=random.randrange(1,100)
gess=1
usg=int(input("PLEASE GEUSS A NUMBER BETWEEN 1 TO 100:  "))
gameover=False
while True:
    if(usg==number):
        print(f"YOU WIN AND GEUSSED THE NUMBER IN {gess} time")
        break
    else:
        if(usg>number):
            gess+=1
            print("TOO HIGH")
            usg=int(input("GESS AGAIN: "))
        else:
            gess+=1
            print("TOO LOW")
            usg=int(input("GESS AGAIN: "))