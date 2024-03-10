import time
from keyflow import kfprint, kfinput

#checks if the username and password are in the database
def check_username_and_password():
    username = kfinput("\nEnter your username: ", speed=0.05)
    #check to see if the username is in the database. if not, ask for username again

    #if the username is legit, check to see if the password is in the database. if not, ask for password again
    password = kfinput("\nEnter your password: ", speed=0.05)

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

kfprint("Hello! Welcome to this awesome gambling game!", speed=0.05)
introduction()
