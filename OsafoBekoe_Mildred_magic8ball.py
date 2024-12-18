import random                                                            # Imports Library
answers = ['Yes','No','Maybe','Ask again later']                         # Creates answer list
question_words = ['Who','What','When','Where','Why', 'Will']             # Creates question words list that user MUST start with
while True:                                                              # Start loop
    ask = input("What would you like to ask? Press enter to quit. Start your question with: 'Who','What','When','Where','Why', and 'Will.'") # Allows user to respond

    if ask=="":                                                          # Allows user to exit
        print("You are leaving the game.")
        break
    first_word = ask.split()[0]                                          # Splits response into list to identify first word
    if "?" in ask or first_word.capitalize() in question_words:          # If it is a question or starts with a question mark, computer responds
        responses = random.choice(answers)                               # User response = Random answer in "answers" list
        print(responses)                                                 # Shows user response
    else:                                                                # Anything else is not going to be answered
        print("Not a question!")