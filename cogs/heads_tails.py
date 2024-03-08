#make sure that the time is spaces (appropriate time between each print statement)
import time
import random
from keyflow import kfprint, kfinput
array = ['heads' , 'tails']
#score = from database

#input validation
def input_validation():
    loop = True
    while loop == True:
        choice_user = str(kfinput("Choose: \n*Heads \n*Talis \nPut answer here: ", speed=0.2))
        choice_user = choice_user.lower()
        if choice_user in array:
            time.sleep(1.5)
            print(f"Ok, you have chosen: {choice_user}")
            loop = False
            heads_tails_game(choice_user)

        else:
            print("Please look at the options, and try again.")
            time.sleep(1)



#game chooses heads or tails
def heads_tails_game(choice_user):
    place_holder = random.randint(0, 1)
    choice_game = array[place_holder]

    print("The results are in!")
    time.sleep(1.5)
    print("And you are...")

    #choices
    if choice_game == choice_user:
        print("Lucky! You got it right. Heres 'x' amount of points.")
        #decrease score from database
    else:
        print("Unlucky. You lost 'x' amount of points. Better luck next time.")
        #decrease score from database




#introduction
print("Welcome to heads or tails.")
time.sleep(1.5)
input_validation()