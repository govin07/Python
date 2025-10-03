import random

jackPort = random.randint(1,100)
print(jackPort)

guessNumber = int(input("guess the number ? "))

while  guessNumber != jackPort:
    if guessNumber < jackPort:
        print("guess higher")
    else :
        print("guess  lower")
    
    guessNumber = int(input("guess again "))

print("your are correct")