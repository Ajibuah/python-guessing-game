import random

randomNumbers = random.randint(1,100)
userChoice = 0

while userChoice != randomNumbers:
    userChoice = int(input("Guess the First number in my mind: "))
    userchoice_a = int(input("Guess the Second number in my mind: "))
    userchoice_b = int(input("Guess the Third number in my mind: "))
    userchoice_c = int(input("Guess the Fourth number in my mind: "))
    userchoice_d = int(input("Guess the Fifth24 number in my mind: "))

    if userChoice < randomNumbers:
        print("Your choice is too low!")

    elif userChoice > randomNumbers:
        print("Your choice is too high!")

print("You've quessed correcty!")