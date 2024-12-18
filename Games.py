import random                                                                                         #Imported a library

def print_colored_text(text, color_name):                                                             #Enabling text and color
    colors = {                                                                                        #Introducing colors
        'black': '\033[30m',                                                                          
        'red': '\033[31m',                                                                            
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',                                                                           # Reset to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')                                           # Default to white if color not found
    print(f"{color_code}{text}\033[0m")                                                               # Print text with color and reset
  
def input_colored_text(text, color_name):                                                            #Allowing color within an input
  colors = {
      'black': '\033[30m',
      'red': '\033[31m',
      'green': '\033[32m',
      'yellow': '\033[33m',
      'blue': '\033[34m',
      'magenta': '\033[35m',
      'cyan': '\033[36m',
      'white': '\033[37m',
      'reset': '\033[0m',                                                                             # Reset to default
  }
  
  color_code = colors.get(color_name.lower(), '\033[37m')                                             # Default to white if color not found
  return input(f"{color_code}{text}\033[0m")                                                          # Print text with color and reset 

points = 0 
game = input("Which game would you like to play? Numbers, Colors, or All About Me?")                  # Initiates and asks game
if game == "numbers":                                                                                 #Loop based on answrs
        number = random.randint(1,100)                                                                # Generate a random number
        guesses = 0                                                                                   # User guesses
        while True:
            try:
              guess = int(input("Guess a number between 1 and 100:"))                                 # Asks user
              if guess < 1 or guess > 100:        
                print("Invalid guess. Please enter a number between 1 and 100.")                      # No answers excepted less than 1 and greater than 100
              elif guess < number:                                                                    # Too low or too high, try again
                print("Too low, try again!")
                guesses += 1
              elif guess > number:
                print("Too high, try again!")
                guesses += 1
              else:
                print("Congratulations! You guessed the number correctly!")                           # User guesses correct and game breaks
                guesses += 1
                break
            except ValueError:                                                                        # If no number is inputed
              print("Invalid input. Please enter a number.")
        print(f"it took you {guesses} guesses")                                                       # Tells user how many tries it took

elif game == "Colors":                                                                                # If user picks colors
  colors = ['red', 'black', 'green', 'yellow','blue', 'magenta', 'cyan', 'white']                     # Printing colors
  print("Type the color that you see! The game ends once your streak ends. Choose from red, black, green, yellow, blue, magenta, cyan, or white. Say 'Done' when you're finished with the game.")

  while True:                                                                                         # Directions Loop
    answer= input("Understand? Yes or No")
    if answer == "Yes":
      break
    elif answer == "No":
      print("Type the color you see, not the color you read.Try until you get it wrong, then you have to reset. Choose from red, black, green, yellow, blue, magenta, cyan, or white. Say 'Done' when you're finished with the game.")
    else:
      print("invalid")
  streak = 0                                                                                          # Starting game
  while True:
    color = random.choice(colors)                                                                     # Defines color of the word to be random
    word = random.choice(colors)                                                                      # Defines colors to be random
    response = input_colored_text(word, color)                                                        
    if response == "Done":                                                                            # Allows user to leave
      exit()
    elif response == color:
      print("You got it!")
      streak += 1                                                                                     # Adds a point to the streak
    else:
      streak == 0                                                                                     # Resets streak
      print(f"Streak broken, try again! You're highest streak was {streak}.")                         # Tells them the number       

elif game == "All About Me":                                                                          # If user picks this option
  points = 0                                                                                         # Points starts at 0
  response = input("When's my birthday?")                                                             # Question
  if response == "November 3rd" "Nov 3rd" "Nov 3" "11/3":                                             # Correct answer
    print("Correct, Good Job!")
    points += 1                                                                                       # Adds a point
  elif response != "November 3rd" "Nov 3rd" "Nov 3" "11/3":                                           # Wrong answer
    print("Wrong! Not good...")
  else:
    print("Invalid response")

                                                                                                      #Same process over and over
  response == input("Favorite color?")
  if response == "Purple":
    print ("Correct, Good Job!")
  elif response != "Purple":
    print("Wrong! Do better...")
  else: print("Invalid response")
  response == input("Summer, Spring, Winter, or Fall?")
  if response == "Spring":
    print ("Correct, Good Job!")
  elif response != "Spring":
    print("Wrong! Do better...")
  else: print("Invalid response")
  
  print(f"This game was just for fun, hope you liked it! You got {points}/2 right")

  
