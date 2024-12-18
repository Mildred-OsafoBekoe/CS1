import random                                                                                         # Imported a library

def print_colored_text(text, color_name):                                                             # Enabling text and color
    colors = {                                                                                        # Introducing colors
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
  
colors = ['red', 'black', 'green', 'yellow','blue', 'magenta', 'cyan', 'white']                       # Creates a color list 
user_name = input("Hello user! Welcome to the random color game. What is your name?  ")               # Prompts user for a response

while True:
    rules = input(f"Welcome {user_name}! Ready to learn the rules? y or n?  ")                        # Inputs last response, Prompts user for a new response

    if rules == "n":                                                                                  # If user response is no
        no_response = input("Waiting... Ready? (y or n)  ")                                           # Prompts user for a response
        
        if no_response == "y":                                                                        # If user response is yes
            break                                                                                     # Continues to next piece of code
        elif no_response == "n":                                                                                         # Anything other than yes
            continue                                                                                  # Start the loop again
        else:
            print("Invalid")
            continue
    elif rules == "y":                                                                                # If user response is yes
        print("Type the color that you see! The game ends once your streak ends. Choose from red, black, green, yellow, blue, magenta, cyan, or white. Say 'Done' when you're finished with the game.")
        answer= input("Understand? Yes or No").lstrip()                                               # Prompts user for a response
        
        if answer == "Yes":                                                                           # If user response yes
            break                                                                                     # Breaks from loop, continues to the next piece of code
        elif answer == "No":                                                                          # If user response no
            print("Type the color you see, not the color you read.Try until you get it wrong, then you have to reset. Choose from red, black, green, yellow, blue, magenta, cyan, or white. Say 'Done' when you're finished with the game.")
            continue
        else:                                                                                         # Anything other than yes or no
            print("invalid")
            continue
    else:
        print("Invalid")
streak = 0                                                                                            # Streak variable, set to 0
highest_streak = 0                                                                                    # Highest streak variable, set to 0

while True:                                                                                           # While true loop
    color = random.choice(colors)                                                                     # Defines color of the word to be random
    word = random.choice(colors)                                                                      # Defines colors to be random
    print_colored_text(word, color)                                                                   # Printed colored texted(defined earlier) 
    response = input('Enter color: ')                                                                 # Prompts user for response

    if response == "Done":                                                                            # Allows user to leave
        break
    elif response == color:                                                                           # If response  is equal to random color generated
        print("You got it!")
        streak += 1                                                                                   # Adds a point to the streak
    else:                                                                                             # If responses are not equal
        if streak > highest_streak:                                                                   # If current streak is higher than highest_streak
            highest_streak = streak                                                                   # Current streak replaces last streak (If higher)
        streak = 0                                                                                    # Resets streak
        print(f"Streak broken, try again! You're highest streak was {highest_streak}.") 