import random #Imports library
mains = ['Cauliflower', 'tilapia fillet', 'pork loin', 'salmon', 'potatoes', 'three color squash', 'eggplant', 'steak', 'baguette'] #Creates list of mains
mains_prices = [20, 25, 28, 30, 18, 20, 22, 30, 20] #List of main prices
flairs = ['with balsamico', 'with garlic and olive oil', 'with minted yogurt', 'with chutney', 'salad', 'with salsa', 'over sticky rice', 'au jus', 'with basmati rice'] #Creates list of flairs
deserts = ['Chocolate Cake', 'Classic New York Cheesecake', 'Strawberry Swirl Cheesecake', 'Fudge Brownies', 'Brownie Sundae', 'Lemon Meringue Pie', 'Apple Crumble Cheesecake', 'Creme Brulee','Chocolate Lava Cake','Italian Tiramisú'] #Creates list of deserts
deserts_prices = [25,30,30,20,18,25,30,33,30,35] #List of desert prices
drinks = ['Shirley Temples', 'Virgin Margaritas', 'Virgin Piña Coladas', 'Coke','Lemonade','Water', 'Iced Tea','Cranberry Juice', 'Sprite', 'Mountain Dew', 'Ginger Ale'] #Creates list drinks
drink_price = 5 #Declares drink price

while True: #Starts infinite loop
    try: #Will test for errors, no errors it will continue
        order = int(input("Welcome to the Food-o-matic! How many orders will you be taking? "))
    except ValueError: #If user doesn't enter a number
        print('Enter a number')
        continue #Continue, means to go back to the start of the loop, so in this case it would prompt the question again

    total = 0 #Declaring the starting value for toal price
    used = [] #Creates empty list

    for i in range (order): #For every value in order
        main = random.choice(mains) #Chooses a random main in the list of mains
        flair = random.choice(flairs) #Chooses a random flair in the list of flairs
        drink = random.choice(drinks) #Chooses a random drink in the list of drinks

        if main + flair in used: #if main and flair have been used, generate again
            continue
        used.append(main + flair) #add main+flair to used list

        main_price = mains_prices[mains.index(main)] #Gets the index of mains

        print(f'The dish is {main} {flair} and the drink is {drink}')

        done = input("Are you satisfied with your order? y or n? ") # Ask user if they like they're order

        if done == "y":
            print("Great! Enjoy your food!")
        elif done == "n":
            change = input("What you like to change? Main, flair, or drink? You cannot change deserts, they are already being made. ").lower() #Changing input to all lowercase
            
            if change == "main":
                main = input("What is the main part of your dish? ")
            elif change == "flair":
                flair = input("What is the flair part of your dish? ")
            if change == "drink":
                drink = input("What is the drink part of your dish? ")
        desert = random.choice(deserts) #Chooses random desert in list deserts
        desert_price = deserts_prices[deserts.index(desert)] #Gets the index of deserts
        print(f'{main} {flair} and {drink} and {desert}, ${main_price} + ${desert_price} + ${drink_price} = ${main_price + desert_price + drink_price}') #Adds up all prices
        total += main_price + desert_price + drink_price
    print(total) #Print total

    play_again = input("Restart? ")
    if play_again == "n":
        break
    if play_again == "y":
        continue
    else:
        print("Please enter y or n.")
        continue
