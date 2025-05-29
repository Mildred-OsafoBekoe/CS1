import csv
import random
import time
import os
'''
Author: Mildred Osafo-Bekoe
Date: 5/22/25
Description: Password Keeper that allows user to interact with a series of prompts pertaining users inputted websites, usernames, passwords.

Challenges: 
- Allows the user to retroactively add more usernames and passwords
- Allows the user to change usernames and passwords
- Check how complex/secure the passwords are
- Require a password to enter the password keeper
- Generate a secure password for the user
- Challenges inside challenges :)

Bugs: None... that I know of.
Sources: https://www.w3schools.com/python/default.asp
'''

def export_to_csv(filename, headers, *arrays):
    '''
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    Returns:
        None
    '''
                                                                                               #First  have to make sure caller actually gave program at least one list to write
    if not arrays:                                                                             #If no arrays, program cannot form any rows-stop with an error
        raise ValueError("At least one array must be provided.")
    
    num_rows = len(arrays[0])                                                                  #Remember how many rows we can expect, which is the length of the first array
    
                                                                                               #Checking that every other array has that same length
    for arr in arrays:
        if len(arr) != num_rows:                                                               #If any list is shorter or longer, it cannot be zipped into rows
            raise ValueError("All arrays must have the same length.")
    
    with open(filename, 'w', newline='') as csvfile:                                           #Open the file for writing. 'newline=""' avoids blank lines on Windows.
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)                                                            #Write the header row first

                                                                                               #Now is writing one data row at a time. Loop from 0 up to num_rows-1, and pull that index out of each array.
        for i in range(num_rows):                                                              #Build a single row: the i-th element from each column list.
            row = [arr[i] for arr in arrays]                                                   #Collects each array’s i-th item, for each arr in arrays, take arr[i]
            csvwriter.writerow(row)                                                            #Write that row into the CSV, and automatically adds commas between items.

def add_entry(websites, usernames, passwords):
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords
    '''
    website = input("Hello, please enter a website: ")
    websites.append(website)
    username = input("Enter the username for this website: ")
    usernames.append(username)
    password = input("Enter the password (press 'g' to generate): ")

    if password.lower() == "g":
        password = generate_password()
    passwords.append(password)

def print_entry(website, username, password):
    '''
   Takes three elements (a website, username, and password trio) and prints them neatly in an f-string

    Args:
        websites (str): the given website
        usernames (str): the given username
        passwords (str): the given password
    Returns:
        print: given entry
    '''
    print(f'''Here is your saved password:
    Website: {website}
    Username: {username}
    Password: {password}''')

def print_entries(websites, usernames, passwords):
    '''
   Takes three elements (a website, username, and password trio) and prints them neatly in an f-string

    Args:
        websites (str): the given website
        usernames (str): the given username
        passwords (str): the given password
    Returns:
        print: given entries
    '''
    for website, username, password in zip(websites, usernames, passwords):
        print(f'''
Website: {website}
Username: {username}
Password: {password}
''')
        
def get_index(websites):
    '''
    Takes the list of websites. Prompts the user for a website and returns the index of that website in the given list of websites.

    Args:
        websites (list): the list of websites
    Returns:
        int: index of that website in the given list of websites
    '''
    while True:
        find_website = input("Which website are you looking for? ")

        if find_website in websites:
            return websites.index(find_website)                                                #Finds the website in websites list and returns the index of that website

def change_entry(websites, usernames, passwords):
    '''
    Takes the list of websites. Prompts the user for a website and returns the index of that website in the given list of websites.

    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    '''
    index = get_index(websites)                                                                #The Index is the index of the inputted website in the list websites

    while True:
        change_type = input('What would you like to change? (Enter "q" to stop) password ("p") or username ("u") ').lower()

        if change_type == "q":
            break
        elif change_type == "p":
            passwords[index] = input(f'Enter new password for {websites[index]}: ')            #The index of the inputted password will be replaced with the new inputted password.
        elif change_type == "u":
            usernames[index] = input(f'Enter new username for {websites[index]}: ')            #The index of the inputted username will be replaced with the new inputted username.
        else:
            print('Invalid')

def delete_entry(websites, usernames, passwords):
    '''
    Deletes a given entry
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    '''
    index = get_index(websites)
    websites.pop(index)
    usernames.pop(index)                                                                        #Removes website as specific index of input
    passwords.pop(index)

def get_password_length():
    '''
    Ask the user for their desired length for password.

    Args:
        None
    '''
    while True:                                                                                 #Forever Loop
        try:                                                                                    #Check for errors before moving on
            length = int(input('How many characters would you like your password to be?:  '))   #Prompts user to pick a length of password
            if length < 4:
                print('Please enter a length of at least 4')
                continue
            return length
        except ValueError:                                                                      #If input is not an integer
            print("Not an integer!")

def generate_password():
    '''
    Uses password length function to generate a random password from random characters with list.

    Args:
        None
    Returns:
        str: Secure password string
    '''

    length = get_password_length()                                                              #Calls the get length function to get password length

    while True:
        pwd = ''.join(random.sample(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_+<>'), length)) 
                                                                                                #Picks random characters in list that is also the same length as desired length

        if check_security(pwd, length, False):
            print(f'The generated password is {pwd}')                                                                             
            return pwd

def check_security(pwd, length, display):
    '''
    Make sure users inputed password follows the mixed-case, digit, special-char, and minimum-length rules.

    Args:
        pwd (str): The password to check.
        length (int): Minimum required length.
        display (bool): If True, print secure/not secure.

    Returns:
        bool: True if all requirements are met, False otherwise.
    '''
    if len(pwd) < length or pwd == pwd.lower() or pwd == pwd.upper() or not any(char.isdigit() for char in pwd) or not any(char in pwd for char in list('`~!@#$%^&*()_+<>')): # If password is shorter than length, all lowercase, all uppercase, has no digits, and/or has no special characters, the password is not secure. If everything is true, the password is secure.
        if display:
            print(f'{pwd} not secure')
        return False
    else:
        if display:
            print(f'{pwd} secure')
        return True

def clear_console(delay):
    '''
    Clears the console after a given delay.

    Args:
        delay (int): Number of seconds to wait before clearing the console.

    Returns:
        None
    
    '''
    time.sleep(delay)
    os.system('cls')

def enter_password(password, tries):
    '''
     Prompts the user to enter a password, verifying it against a stored password with a limited number of attempts.

    Args:
        password (str): The correct password to compare against.
        tries (int): The number of attempts allowed.

    Returns:
        bool: True if password is correct within allowed attempts; otherwise exits the program.
    '''

    for i in range(tries):
        authentication = input("Please enter your password. ")

        if authentication == password:
            print('You are in!')
            clear_console(1)
            return True
        else:
            print(f"Access denied, please try again. You have {tries-i-1} tries left.")
    print('You are banned!')
    clear_console(1)
    exit()

def change_password(passwords):
    '''
    Allows the user to change the master password either by generating a new one or entering their own.

    Args:
        passwords (list): The list of stored passwords, with the most recent one being the current password.

    Returns:
        str: The newly changed password.
    '''
    enter_password(passwords[-1], 3)

    while True:
        pass_type = input("Would you like to generate a password (g) or make your own (m)? ").lower()
        
        if pass_type == "g":
            new_password = generate_password()
            passwords.append(new_password)
            return new_password
        elif pass_type == "m":
            while True:
                new_password = input("Please enter your desired password: ")

                if new_password in passwords:
                    print("You cannot reuse an old password.")
                else:
                    passwords.append(new_password)
                    print(f"Password succesfully changed to {new_password}.")
                    return new_password
        else:
            print('Invalid')

def main():
    websites = []
    usernames = []
    passwords = []
    codes = []

    password = input('Enter your secret password: ')
    clear_console(2)
    codes.append(password)
    enter_password(password, 3)

    while True:
        option = input('''Which would you like to do? Enter "q" to quit
1. Add an entry
2. Print an entry
3. Print all entries
4. Change an entry
5. Delete an entry  
6. Generate a password
7. Check the security of a password
8. Export entries to a csv
9. Change Password Keeper Password                     
    ''').lower()
        
        if option == "q":
            print("Thank you for using the Password Keeper. Made by Mildred Osafo-Bekoe")
            break
        elif option == "1":
            add_entry(websites, usernames, passwords)
        elif option == "2":
            index = get_index(websites)
            print_entry(websites[index], usernames[index], passwords[index])
        elif option == "3":
            print_entries(websites, usernames, passwords)
        elif option == "4":
            change_entry(websites, usernames, passwords)
        elif option == "5":
            delete_entry(websites, usernames, passwords)
        elif option == "6":
            pwd = generate_password()
            store = input('Would you like to store this password for a specific entry? y/n ')

            if store.lower() == "y":
                index = get_index(websites)
                passwords[index] = pwd
        elif option == "7":
            pwd = input('Enter a password or "p" to access a specific entry: ')

            if pwd.lower() == "p":
                index = get_index(websites)
                pwd = passwords[index]
            default_min_length = 4
            check_security(pwd, default_min_length, True)
        elif option == "8":
            filename = input('Enter the filename for your csv: ')
            export_to_csv(filename+".csv", ["Website", "Username", "Password"], websites, usernames, passwords)
            print(f'Data successfully exported to {filename}.csv')
        elif option == "9":
            change_password(codes)
        else:
            print('invalid')
main()