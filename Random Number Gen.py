import random

game = input("Which game would you like to play? Numbers, Colors, or All About Me?")
if game == numbers:
        # Generate a random number
        number = random.randint(1,100)
        guesses = 0
        # User guesses
        while True:
            try:
              guess = int(input("Guess a number between 1 and 100:"))
              if guess < 1 or guess > 100:
                print("Invalid guess. Please enter a number between 1 and 100.")
              elif guess < number:
                print("Too low, try again!")
                guesses += 1
              elif guess > number:
                print("Too high, try again!")
                guesses += 1
              else:
                print("Congratulations! You guessed the number correctly!")
                guesses += 1
                break
            except ValueError:
              print("Invalid input. Please enter a number.")
        print(f"it took you {guesses} guesses")


elif game == "colors":
        Colors = 'Red' 'Orange''Yellow' 'Green' 'Blue'
        print("Type the color that you see!")
        print(Fore.RED + 'some red text')

