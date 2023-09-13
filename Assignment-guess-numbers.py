import random

randomNumbers = random.randint(1, 100)
userChoice = 0
chance = 5
print("The number guessing game")
print(f"You have the {chance} to guess the number correctly from 1-100")
while userChoice != randomNumbers:
    userChoice = int(input("Guess the First number in my mind: "))

    if userChoice < randomNumbers:
        print("Your choice is too low!")

    elif userChoice > randomNumbers:
        print("Your choice is too high!")
if userChoice == randomNumbers:
    print(f"You've guessed correctly! The number was {randomNumbers}.")
else:
    print("You've quessed correcty!")
