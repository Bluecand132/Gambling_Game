import time
import sqlite3
from keyflow import kfprint, kfinput

#checks if the username and password are in the database
def check_username_and_password():
    check_username = kfinput("\nEnter your username: ", speed=0.05)
    if check_username == 'Back':
        kfprint("\nOkay, let's go back.", speed=0.05)
        introduction()
    else:
        check_username_in_database(check_username)
    
    check_password = kfinput("\nEnter your password: ", speed=0.05)
    if check_password == 'Back':
        kfprint("\nOkay, let's go back.", speed=0.05)
        introduction()
    else:
        check_password_in_database(check_password)
    
    #give them options for the games to play



#checks to see if username is in the database
def check_username_in_database(check_username):
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()

    #checks to see if username is in database
    cursor.execute("SELECT * FROM user_table WHERE username = ?", (check_username,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        kfprint("\nSorry, this username doesn't exist.", speed=0.05)
        kfprint("\nTry again.", speed=0.05)
        check_username_and_password()

#checks to see if password is in the database
def check_password_in_database(check_password):
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()

    #checks to see if password is in database
    cursor.execute("SELECT * FROM user_table WHERE password = ?", (check_password,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        kfprint("\nSorry, this password doesn't exist.", speed= 0.05)
        kfprint("\nTry again.", speed=0.05)
        check_username_and_password()

#creates username and password
def create_username_and_password():
    loop = True
    kfprint("\nIf you ever want to go to the introduction, type 'Back' at any time.", speed=0.05)
    time.sleep(0.5)
    while loop:
        username = kfinput("\nEnter a username: ", speed=0.05)
        if username == 'Back':
            time.sleep(0.5)
            kfprint("\nOk, let's go back.", speed=0.05)
            introduction()
        else:
            password = get_password()
            confirm_password(password)
            time.sleep(0.5)
            kfprint("\nTime to put you in the database.", speed=0.05)
            put_username_and_password_to_database(username, password)
            loop = False

def get_password():
    loop = True
    while loop:
        password = kfinput("\nEnter a password: ", speed=0.05)
        if password == 'Back':
            kfprint("\nOk, let's go back.", speed=0.05)
            introduction()
            loop = False
        else:
            return password
            
#confirms password from user
def confirm_password(password):
    loop = True
    while loop:
        password_confirmation = kfinput("\nConfirm your password: ", speed=0.05)
        time.sleep(0.5)
        if password_confirmation == 'Back':
            kfprint("\nOk, let's go back.", speed=0.05)
            introduction()
            loop = False
        elif password_confirmation == password:
            kfprint("\nOk, you have entered your username and password.", speed=0.05)
            loop = False
        else:
            kfprint("\nThe passwords do not match. Going back to sign in.", speed=0.05)
            create_username_and_password()
            loop = False

#puts username and password to the database
def put_username_and_password_to_database(username, password):
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()

    #puts username and password in the database
    cursor.execute("INSERT INTO user_table (username, password) VALUES (?,?)", (username, password))

    #puts username and password to the score_table
    cursor.execute("INSERT INTO score_table (balance, wins, losses, draws, avg_wins, avg_losses, avg_draws) VALUES (?,?,?,?,?,?,?)", (50, 0, 0, 0, 0, 0, 0))
    
    #saves and closes the connection
    connection.commit()
    connection.close()



#introduction
def introduction():
    time.sleep(0.5)
    kfprint("\nIf you have a username or password, please enter number '1'.", speed=0.05)
    time.sleep(0.2)
    kfprint("\nOtherwise, please enter number '2'.", speed=0.05)

    #chooses 1 or 2
    while True:
        try:
            if_user = int(kfinput("\nEnter here: ", speed=0.05))
            time.sleep(0.5)
            if if_user == 1:
                kfprint ("\nOk, let's check your username and password.", speed=0.05)
                time.sleep(0.5)
                check_username_and_password()
                break
            elif if_user == 2:
                kfprint("\nOk, let's create you a username and password.", speed=0.05)
                time.sleep(0.5)
                create_username_and_password()
                break
            else:
                kfprint("\nThe input you entered is not valid. Please try again.", speed=0.1)
        except ValueError:
            kfprint("\nThe input you entered is not valid. Please try again.", speed=0.1)
            continue

#starts the thingy!!!
kfprint("Hello! Welcome to this awesome gambling game!", speed=0.05)
introduction()
