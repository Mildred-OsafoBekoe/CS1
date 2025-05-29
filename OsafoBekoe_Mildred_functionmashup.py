import random

def chorus ():
    '''
    Prints the chorus of a song
    Args:
        None
    Returns:
        print: chorus
    '''
    print ("""
I wanna thrill you like Michael
I wanna kiss you like Prince
Let's get it on like Marvin Gaye, like Hathaway
Write a song for you like this

You're over my head, I'm out of my mind
Thinking I was born in the wrong time
One of a kind, living in a world gone plastic""")
    
def sing_song():
    '''
    Prints the whole song.
    Args:
        None
    Returns:
        print: verse, chorus
    '''
    print('''
Ooh, girl, you're shining like a 5th Avenue diamond
And they don't make you like they used to, you're never going out of style
Ooh, pretty baby, this world might have gone crazy
The way you saved me, who could blame me when I just wanna make you smile?
    ''')
    chorus()
    print('''
Four dozen roses, anything for you to notice
All the way to serenade you, doing it Sinatra style
I'ma pick you up in a Cadillac like a gentleman bringing glamour back
Keep it real to real in the way I feel, I could walk you down the aisle
    ''')
    chorus()
    print('''
Baby, you're class and baby, you're sick
I never met a girl like you ever till we met
A star in the '40s, centerfold in the '50s
Got me trippin' out like the '60s, hippies (Oh, woah, woah)
Queen of the discotheque
A '70s dream and an '80s best
Hepburn, Beyoncé, Marilyn, Massive (Ah)
Girl, you're timeless, just so classic
''')
    chorus()

def add(a, b):
    '''
    Takes two numbers and adds them together
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: sum of a and b
    '''
    print(a + b)

def print_list(array):
    '''
    Takes a list and prints every element in that list individually (vertically)
    Args:
        array (list): given list to print
    Returns:
        print: every element in the given list
    '''
    for i in (array):
        print(i)

def in_list(element_to_find, list_of_elements):
    '''
    Takes a list and element and returns a boolean based on if the element is in the list
    Args:
        element_to_find (any): element you are looking for
        list_of_elements (list): list you are given to check
    Returns:
        bool: True/False based on if element_to_find is in list_of_elements
    '''
    return element_to_find in list_of_elements

def get_integer(order):
    '''
    Takes any parameter and returns a boolean based on if it is an integer. Use try/except!
    Args:
        number (any): given parameter to check
    Returns:
        bool: True/False depending on whether number is an integer
    '''
    while True:
        try:
            number = int(input(f"Enter your {order} number "))
            return number
        except ValueError:
            print('Not an integer!')

def get_integers():
    '''
    Asks the user for two numbers, uses is_integer to check input, returns the two integers.
    Args:
        None
    Returns: 
        int: numbers a and b from user input
    '''
    a = get_integer('first')
    b = get_integer('second')
    return a, b
def get_random():
    '''
    Uses get_integers and prints a random number between the two given integers.
    Args:
        None
    Returns:
        print: random int between a and b
    '''
    a, b = get_integers()
    print(random.randint(a, b))

def count_vowels(string):
    '''
    Takes a string and returns the number of vowels in it
    Args:
        string (str): word or phrase to check
    Returns:
        int: number of vowels
    '''
    count = 0

    for char in string: #for every character in string:
        if char in ['a','e','i','o','u']: #if character in ['a', 'e']
            count += 1  #add one to count
    return count

def get_initials(name):
    '''
    Takes a name and returns the initials
    Args:
        name (str): full name
    Returns:
        print: initials
    '''
    names = name.split(' ')
    initials = ''

    for n in names: #for every n in names
        initials += n[0]
    print(initials) #return/print initials

def reverse_string(s):
    '''
    Takes a string and reverses it
    Args:
        none
    Returns:
        print: String in reverse
    '''
    return s[::-1]

def hangman():
    words = ["apple", "brave", "chess", "eagle", "flame", "grape", "heart",
    "ivory", "joker", "kneel", "lemon", "mango", "noble", "ocean", "piano",
    "quake", "raven", "shiny", "tiger", "ultra", "vigor", "whale","young", "zebra"]

    hangman_pics = ['''
+---+
    |
    |
    |
    ===''', '''
+---+
O   |
    |
    |
    ===''', '''
+---+
O   |
|   |
    |
    ===''', '''
-+---+
 O   |
/|   |
     |
     ===''', '''
-+---+
 O   |
/|\  |
     |
    ===''', '''
-+---+
 O   |
/|\  |
/    |
     ===''', '''
-+---+
 O   |
/|\  |
/ \  |
     ===''']
    
    word = random.choice(words)
    word_list = list(word)
    display = [ ]

    for char in word:
        display.append('_')
    
    guesses = 0

    while guesses < 6 and "_" in display:
        guess = input("Hi user, let's play hangman! Input a value:")

def main():
    while True:
        options = input("What would you like to do? Sing a Song (1), Add Two Numbers (2), Print A List Vertically (3), Check if a value is in a list (4), Checks if a value is an integer (5), Prints a random number(6), Count Vowels in a Phrase(7), Print Initials(8), Reverse your input(9), OR play Wordle(10)?")
    
        if options == "1":
            sing_song()
        elif options == "2":
            a, b = get_integers()
            add(a, b)
        elif options == "3":
            print_list(['Pinapple', 'Apple', 'Banana', 'Lemon','Strawberries'])
        elif options == "4":
                user_list = input('Enter a list (use spaces to separate items) ').split(' ')
                check = input('Enter item to look for ')
                print(in_list(check, user_list))
        elif options == "5":
            print(get_integer)    
        elif options == "6":
            get_random()
        elif options == "7":
            print(count_vowels("Hello how are you today!"))
        elif options == "8":
            user_name = input("What's the name?")
            get_initials(user_name)
        elif options == "9":
            user_phrase= input("Enter a word/sentence/phrase: ")
            reversed_input = reverse_string(user_phrase)
            print(reversed_input)
        elif options == "10":
            word_list = []

main()

