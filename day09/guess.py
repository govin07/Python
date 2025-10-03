import random

jackPort = random.randint(1,100)
print(jackPort)

guessNumber = int(input("guess the number ? "))
counter = 1

while  guessNumber != jackPort:
    if guessNumber < jackPort:
        print("guess higher")
    else :
        print("guess  lower")
    
    guessNumber = int(input("guess again "))
    counter += 1

print("your are correct")
print(f"you tryed {counter} times")