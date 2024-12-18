import random                                                                                                   #Import random
import os
weapons = ['Rock','Paper','Scissors']                                                                           #Creates weapons list
win_solutions = [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper','Rock')]                                 #Creates ways to win list
answers = ['Yes','No','Maybe','Ask again later']                                                                #Creates answers list for 8Ball
question_words = ['Who','What','When','Where','Why', 'Will']                                                    #Creates question words

game_start = input("What would you like to play? Rock, Paper, Scissors (1), Magic 8 Ball (2), or Quit (3). ")   #Ask user what they want to play
if game_start == "1":    
    player1_score = 0
    player2_score = 0                                                                                           #If user picks RPS
    player1_name = input("What is your name? ")
    player_vs_computer = input(f"{player1_name}, do you want to play with a bot(1) or a second player(2)?")                                     #Bot or player?
    if player_vs_computer == "1":                                                                               #If user choses bot
        player2_name = "bot"
    else:
        player2_name = input("Player 2, what is your name? ")
    while True:                                                                                                 #Creates loop
        user_rps = input(f"{player1_name}, you can quit at any time, just press enter. Rock...Paper...Scissors...Shoot!").capitalize()    #Starts game
        if player_vs_computer == "1":
            player2_rps = random.choice(weapons)                                                                    #Bot_rps = Random selection in list
        else:
            os.system("cls")
            player2_rps = input(f"{player2_name}, Rock...Paper...Scissors...Shoot! ").capitalize()
        if user_rps == "":                                                                                #If nothing is said it means they want to exit
            print("You can't quit yet, find out the secret code...")                                        #Print text
            secret_code = input("What's the secret code? Press enter if you want to return to the game.").upper()  #Secret code CHALLENGE
            if secret_code == "":                                                                           #Leaving secret code back to the game
                break                                                                                       #Return to rps loop
            elif secret_code == "SOS":                                                                      #If they get the secret code
                print("Congratulations! You can leave now!")                                                #Print text letting them know they leave
                break
        print(f"{player1_name} chose {user_rps}, while {player2_name} chose {player2_rps}")
        if user_rps == player2_rps:                                                                             #When both players print the same
            print(f"Tie! Scores remain the same.")                     #Tells player that they tied
        elif (user_rps, player2_rps) in win_solutions:                                                          #If player wins              
            player1_score += 1                                                                                      #Addition to score
            print(f"{player1_name} wins")                                                       #Anything other than previous scenarios bot wins
        elif (player2_rps, user_rps) in win_solutions:
            player2_score += 1
            print(f"{player2_name} wins")                                                       #Anything other than previous scenarios bot wins
        else:
            print("Someone entered something invalid")
        print(f"{player1_name}: {player1_score} - {player2_name}: {player2_score}")
if game_start == "2":
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


            



 