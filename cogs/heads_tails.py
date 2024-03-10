import time
import random
from keyflow import kfprint, kfinput
array = ['heads' , 'tails']
#score = from database

#input validation
def input_validation():
    while True:
        choice_user = str(kfinput("\nChoose: \n*Heads \n*Talis \nPut answer here: ", speed=0.05))
        choice_user = choice_user.lower()
        try:
            if choice_user in array:
                time.sleep(1.5)
                kfprint(f"Ok, you have chosen: {choice_user}", speed=0.05)
                heads_tails_game(choice_user)
                break
            else:
                kfprint("Please look at the options and try again.", speed=0.1)
                time.sleep(1)
                continue
        except ValueError:
            kfprint("The input you entered is not valid. Please try again.", speed=0.05)
            continue

#game chooses heads or tails
def heads_tails_game(choice_user):
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
        kfprint("\nUnlucky. You lost 'x' amount of points. Better luck next time.", speed=0.05)
        #decrease score from database

#where game is initialised
kfprint("Welcome to heads or tails.", speed=0.05)
time.sleep(1.5)
input_validation()