import sqlite3
import time
import random
from keyflow import kfprint, kfinput

array = ['heads' , 'tails']

#input validation
def input_validation(username, username_id):
    #gets balance of the player
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM score_table WHERE id = ?", (username_id,))
    balance = cursor.fetchone()[0]
    cursor.close()
    connection.close()

    while True:
        choice_user = str(kfinput(f"\nHello, {username}! This is your balance: {balance} \nNow choose: \n*Heads \n*Talis \nPut answer here: ", speed=0.05))
        choice_user = choice_user.lower()
        try:
            if choice_user in array:
                time.sleep(1.5)
                kfprint(f"Ok, you have chosen: {choice_user}", speed=0.05)
                heads_tails_game(choice_user, username, username_id)
                break
            else:
                kfprint("Please look at the options and try again.", speed=0.1)
                time.sleep(1)
                continue
        except ValueError:
            kfprint("The input you entered is not valid. Please try again.", speed=0.05)
            continue

#game chooses heads or tails
def heads_tails_game(choice_user, username, username_id):
    place_holder = random.randint(0, 1)
    choice_game = array[place_holder]
    time.sleep(1.5)
    kfprint("\nThe results are in!", speed=0.05)
    time.sleep(1.5)
    kfprint("\nAnd you are...", speed=0.2)
    time.sleep(2)

#choices
    if choice_game == choice_user:
        kfprint("\nLucky! You got it right. Heres 'x' amount of points.", speed=0.05)
        #increase score from database
    else:
        kfprint("\nUnlucky... You lost 'x' amount of points. Better luck next time.", speed=0.05)
        #decrease score from database
    retry_game(username, username_id)



def retry_game(username, username_id):
    try_again = kfinput("\nWould you like to try again?\nEnter yes, or no: ", speed=0.05)
    try_again = try_again.lower()
    if try_again == "yes":
        input_validation(username, username_id)
    elif try_again == "no":
        kfprint("\nOk, let's go back.", speed=0.05)
    else:
        kfprint("\nThe input you entered is not valid. Please try again.", speed = 0.05)
        retry_game(username, username_id)