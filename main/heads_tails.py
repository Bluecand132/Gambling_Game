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
        while True:
            #asks player how much they wanna bet
            bet = int(kfinput(f"\nHello, {username}! This is your balance: {balance}\nHow much would you like to bet? Enter here: ", speed=0.05))
            bet = bet * 2
            try:
                if bet < 0:
                    kfprint("\nYou can't bet a negative number. Please try again.", speed=0.5)
                    continue
                elif bet > 0:
                    break
                else:
                    kfprint("\nYou can't bet 0. Please try again.", speed=0.5)
                    continue
            except ValueError:
                kfprint("\nThe input you entered is not valid. Please try again.", speed=0.5)
                continue

        choice_user = str(kfinput("\nOk! Now choose: \n*Heads \n*Talis \nPut answer here: ", speed=0.05))
        choice_user = choice_user.lower()
        try:
            if choice_user in array:
                time.sleep(1.5)
                kfprint(f"Ok, you have chosen: {choice_user}", speed=0.05)
                heads_tails_game(choice_user, username, username_id, bet)
                break
            else:
                kfprint("Please look at the options and try again.", speed=0.5)
                time.sleep(1)
                continue
        except ValueError:
            kfprint("The input you entered is not valid. Please try again.", speed=0.05)
            continue



#game chooses heads or tails
def heads_tails_game(choice_user, username, username_id, bet):
    win_loss = 1
    choice_game = random.choice(array)
    time.sleep(1.5)
    kfprint("\nThe results are in!", speed=0.05)
    time.sleep(1.5)
    kfprint("\nAnd you are...", speed=0.2)
    time.sleep(2)

#choices
    if choice_game == choice_user:
        kfprint(f"\nLucky! You got it right. Heres {bet} amount of points.", speed=0.05)
        #increase score from database
        connection = sqlite3.connect('user_database.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE score_table SET balance = balance + ? WHERE id = ?", (bet, username_id))
        cursor.execute("UPDATE score_table SET wins = wins + ? WHERE id = ?", (win_loss, username_id))
        connection.commit()
        cursor.close()
        connection.close()

    else:
        kfprint(f"\nUnlucky... You lost {bet} amount of points. Better luck next time.", speed=0.05)
        #decrease score from database
        connection = sqlite3.connect('user_database.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE score_table SET balance = balance - ? WHERE id = ?", (bet, username_id))
        cursor.execute("UPDATE score_table SET losses = losses + ? WHERE id = ?", (win_loss, username_id))
        connection.commit()
        cursor.close()
        connection.close()
    retry_game(username, username_id)



#asks player is they want to play again or not
def retry_game(username, username_id):
    try_again = kfinput("\nWould you like to try again?\nEnter yes, or no: ", speed=0.05)
    try_again = try_again.lower()
    if try_again == "yes":
        input_validation(username, username_id)
    elif try_again == "no":
        kfprint("\nOk, let's go back.", speed=0.5)
        time.sleep(1)
    else:
        kfprint("\nThe input you entered is not valid. Please try again.", speed = 0.5)
        retry_game(username, username_id)
