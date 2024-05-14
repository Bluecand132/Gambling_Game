import time
import sqlite3
from keyflow import kfprint, kfinput
import bcrypt
import heads_tails

# checks if the username and password are in the database
def check_username_and_password():
    kfprint("\nIf you ever want to go to the introduction, type 'Back' at any time.", speed=0.05)
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
        #turn inputted password into hashed password, and compare it with hashed password in the database
        check_password_in_database(check_password, check_username)



# checks to see if username is in the database
def check_username_in_database(check_username):
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()

    # checks to see if username is in database
    cursor.execute("SELECT * FROM user_table WHERE username = ?", (check_username,))
    result = cursor.fetchone()

    if result:
        return True
    else:
        #result doesnt RETURN BOOLEAN!!!
        kfprint("\nSorry, this username doesn't exist.", speed=0.05)
        kfprint("\nTry again.", speed=0.05)
        check_username_and_password()



#checks to see if password is in the database
def check_password_in_database(check_password, check_username):
    #takes hashed password from the database
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT password FROM user_table WHERE username = ?", (check_username,))
    password_array = cursor.fetchone()
    password_to_check = password_array[0]

    cursor.close()
    connection.close()

    check_password_enc = check_password.encode('utf-8')
    #checks if password is same as password in database (hashed)
    result = bcrypt.checkpw(check_password_enc, password_to_check)

    if result:
        kfprint("\nPassword matches!", speed=0.05)
        # start giving choices to the user
        time.sleep(0.05)
        user_home(check_username)
    else:
        kfprint("\nSorry, this password doesn't exist.", speed= 0.05)
        kfprint("\nTry again.", speed=0.05)
        check_username_and_password()



#creates username and password
def create_username_and_password():
    kfprint("\nIf you ever want to go to the introduction, type 'Back' at any time.", speed=0.05)
    time.sleep(0.05)
    username = kfinput("\nEnter a username: ", speed=0.05)
    if username == 'Back':
        time.sleep(0.05)
        kfprint("\nOk, let's go back.", speed=0.05)
        introduction()
    else:
        result = check_username_is_usable(username)
        if result:
            kfprint("\nThis username is already in use. Please try again.", speed=0.05)
            create_username_and_password()
        
        else:
            password = get_password()
            confirm_password(password)
            time.sleep(0.05)
            kfprint("\nTime to put you in the database.", speed=0.05)
            put_username_and_password_to_database(username, password)
            return



#check to see if username is usuable
def check_username_is_usable(username):
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()

    #checks to see if username is in database
    cursor.execute("SELECT COUNT(*) FROM user_table WHERE username = ?", (username,))
    result = cursor.fetchone()[0]
    return result > 0



#gets the password from the user
def get_password():
    password = kfinput("\nEnter a password: ", speed=0.05)
    if password == 'Back':
        kfprint("\nOk, let's go back.", speed=0.05)
        introduction()
    else:
        return password



#confirms password from user
def confirm_password(password):
    password_confirmation = kfinput("\nConfirm your password: ", speed=0.05)
    time.sleep(0.5)
    if password_confirmation == 'Back':
        kfprint("\nOk, let's go back.", speed=0.05)
        introduction()
    elif password_confirmation == password:
        kfprint("\nOk, you have entered your username and password.", speed=0.05)
        return
    else:
        kfprint("\nThe passwords do not match. Going back to sign up.", speed=0.05)
        create_username_and_password()



#puts username and password to the database
def put_username_and_password_to_database(username, password):
    #hash the password
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    #connets to database
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()

    #puts username and password in the database
    cursor.execute("INSERT INTO user_table (username, password, salt) VALUES (?,?,?)", (username, hashedPassword, salt))

    #puts username and password to the score_table
    cursor.execute("INSERT INTO score_table (balance, wins, losses, draws, avg_wins, avg_losses, avg_draws) VALUES (?,?,?,?,?,?,?)", (50, 0, 0, 0, 0, 0, 0))
    
    #saves and closes the connection
    connection.commit()
    connection.close()



def user_home(username):
    kfprint(f"\nHello, {username}! What would you like to do?", speed=0.05)
    kfprint("\n1.) Display my stats.", speed = 0.05)
    kfprint("\n2.) Play Heads or Tails.", speed = 0.05)
    kfprint("\n3.) Play Rock, Paper, Scissors.", speed = 0.05)
    choice = int(kfinput("\nEnter here: ", speed = 0.05))

    if choice == 1:
        #display the stats
        connection = sqlite3.connect('user_database.db')
        cursor = connection.cursor()

        cursor.execute("SELECT id FROM user_table WHERE username = ?", (username,))
        username_id = cursor.fetchone()[0]
        cursor.execute("SELECT * FROM score_table WHERE id = ?", (username_id,))
        stats = cursor.fetchone()
        kfprint(f"\nBalance: {stats[1]}\nWins: {stats[2]}\nLosses: {stats[3]}\nDraws: {stats[4]}\nAverage Wins: {stats[5]}\nAverage Losses: {stats[6]}\nAverage Draws: {stats[7]}", speed = 0.05)
        cursor.close()
        connection.close()
        back_input = kfinput("\nWhen you're ready, type 'Back' to go back to the main menu.\n", speed = 0.05)
        
        while True:
            try:
                if back_input == 'Back':
                    user_home(username)
                    break
                else:
                    kfprint("\nTry again.", speed = 0.05)
                    continue
            except ValueError:
                kfprint("\nThe input you entered is not valid. Please try again.", speed = 0.05)
                continue
    
    elif choice == 2:
        #play heads or tails
        kfprint("Welcome to heads or tails.", speed=0.05)
        time.sleep(1.5)
        heads_tails.input_validation()
    
    elif choice == 3:
        #play rock, paper, scissors
        print("balls")
    
    else:
        kfprint("\nThe input you entered is not valid. Please try again.", speed=0.05)
        user_home(username)



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