import random as r
number_random = r.randint(1, 10)

while True:
    option = int( input("Guess the number: "))
    if option != number_random:
        print("You failed, try again.")
    else:
        break
print("Congratulations, you guessed it.")