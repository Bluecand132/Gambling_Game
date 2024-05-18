import random
import time
import sqlite3
from keyflow import kfprint, kfinput

array = ['rock', 'paper', 'scissors']

#initiates the game
def rock_paper_scissors_game(username, username_id):
    #this loop makes sure the bet is good
    while True:
        try:
            connection = sqlite3.connect('user_database.db')
            cursor = connection.cursor()
            cursor.execute("SELECT balance FROM score_table WHERE id = ?", (username_id,))
            balance = cursor.fetchone()[0]
            bet = int(kfinput(f"\nHello, {username}! This is your balance: {balance}\nHow much would you like to bet? Enter here: "), speed = 0.05)
            time.sleep(0.5)
            if bet < 0:
                kfprint("\nYou can't bet a negative number. Please try again.", speed=0.5)
                continue
            elif bet > 0:
                bet = bet * 3
                break
            else:
                kfprint("\nYou can't bet 0. Please try again.", speed = 0.5)
                continue
        except ValueError:
            kfprint("\nThe input you entered is not valid. Please try again.", speed = 0.5)
            continue

    #this loop has the game
    while True:
        try:
            choice_user = str(kfinput("\nOk! Now choose: \n*Rock\n*Paper\n*Scissors\nPut answer here: ", speed = 0.05))
            time.sleep(0.5)
            choice_user = choice_user.lower()
            
            choice_game = random.choice(array)
            win_loss_draw = 1

            kfprint("\nThe bot has made its decision!", speed = 0.05)
            time.sleep(1.5)
            kfprint("\nAnd the results are...", speed = 0.2)
            time.sleep(2)

            if choice_user == choice_game:
                kfprint("It's a tie! You get nothing.", speed = 0.05)
                connection = sqlite3.connect('user_database.db')
                cursor = connection.cursor()
                cursor.execute("UPDATE score_table SET draws = draws + ? WHERE id = ?", (win_loss_draw, username_id))
                connection.commit()
                cursor.close()
                connection.close()
                break

            elif choice_user == 'rock' and choice_game == 'scissors':
                kfprint("You win! Rock beats scissors!", speed = 0.05)
                connection = sqlite3.connect('user_database.db')
                cursor = connection.cursor()
                cursor.execute("UPDATE score_table SET balance = balance + ? WHERE id = ?", (bet, username_id))
                cursor.execute("UPDATE score_table SET wins = wins + ? WHERE id = ?", (win_loss_draw, username_id))
                connection.commit()
                cursor.close()
                connection.close()
                break

            elif choice_user == 'rock' and choice_game == 'paper':
                kfprint("You lose! Paper beats rock!", speed = 0.05)
                connection = sqlite3.connect('user_database.db')
                cursor = connection.cursor()
                cursor.execute("UPDATE score_table SET balance = balance - ? WHERE id = ?", (bet, username_id))
                cursor.execute("UPDATE score_table SET losses = losses + ? WHERE id = ?", (win_loss_draw, username_id))
                connection.commit()
                cursor.close()
                connection.close()
                break

            elif choice_user == 'paper' and choice_game == 'rock':
                kfprint("You win! Paper beats rock!", speed = 0.05)
                connection = sqlite3.connect('user_database.db')
                cursor = connection.cursor()
                cursor.execute("UPDATE score_table SET balance = balance + ? WHERE id = ?", (bet, username_id))
                cursor.execute("UPDATE score_table SET wins = wins + ? WHERE id = ?", (win_loss_draw, username_id))
                connection.commit()
                cursor.close()
                connection.close()
                break

            elif choice_user == 'paper' and choice_game == 'scissors':
                kfprint("You lose! Scissors beats paper!", speed = 0.05)
                connection = sqlite3.connect('user_database.db')
                cursor = connection.cursor()
                cursor.execute("UPDATE score_table SET balance = balance - ? WHERE id = ?", (bet, username_id))
                cursor.execute("UPDATE score_table SET losses = losses + ? WHERE id = ?", (win_loss_draw, username_id))
                connection.commit()
                cursor.close()
                connection.close()
                break

            elif choice_user == 'scissors' and choice_game == 'rock':
                kfprint("You lose! Rock beats scissors!", speed = 0.05)
                connection = sqlite3.connect('user_database.db')
                cursor = connection.cursor()
                cursor.execute("UPDATE score_table SET balance = balance - ? WHERE id = ?", (bet, username_id))
                cursor.execute("UPDATE score_table SET losses = losses + ? WHERE id = ?", (win_loss_draw, username_id))
                connection.commit()
                cursor.close()
                connection.close()
                break

            elif choice_user == 'scissors' and choice_game == 'paper':
                kfprint("You win! Scissors beats paper!", speed = 0.05)
                connection = sqlite3.connect('user_database.db')
                cursor = connection.cursor()
                cursor.execute("UPDATE score_table SET balance = balance + ? WHERE id = ?", (bet, username_id))
                cursor.execute("UPDATE score_table SET wins = wins + ? WHERE id = ?", (win_loss_draw, username_id))
                connection.commit()
                cursor.close()
                connection.close()
                break

            else:
                kfprint("Please look at the options and try again.", speed = 0.5)
                continue
        
        except ValueError:
            kfprint("The input you entered is not valid. Please try again.", speed = 0.5)
            continue

    retry_game(username, username_id)



#retry the game or not
def retry_game(username, username_id):
    time.sleep(0.5)
    try_again = kfinput("Would you like to try again?\nEnter yes or no: ", speed=0.05)
    time.sleep(0.5)
    try_again = try_again.lower()
    if try_again == "yes":
        time.sleep(0.5)
        rock_paper_scissors_game(username, username_id)
    elif try_again == "no":
        kfprint("Ok, let's go back.", speed=0.5)
        time.sleep(1)
    else:
        kfprint("The input you entered is not valid. Please try again.", speed=0.5)
        retry_game(username, username_id)
