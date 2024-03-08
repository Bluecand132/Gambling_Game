import time
import random
array = ['heads' , 'tails']
#score = from database

#game chooses heads or tails
def heads_tails_game():
    place_holder = random.randint(0, 1)
    choice_game = array[place_holder]

    #choices
    if choice_game == choice_user:
        print("Good job! You got it right. Heres 'x' amount of points.")
        #decrease score from database
    else:
        print("Unlucky, you lost 'x' amount of points. Better luck next time.")
        #decrease score from database




#introduction
print("Welcome to heads or tails.")
time.sleep(1.5)

#user chooses heads or tails
while True:
    try:
        choice_user = str(input("Choose: \n*Heads \n*Talis \nPut answer here: "))
        if choice_user in array:
            print(f"Ok, you have chosen: {choice_user}")
            loop = False
        else:
            print("Please look at the options.")

    except:
        print("Please look at the options.")


'''    except choice_user not in array:
        print("Please look at the options.")
        continue
    else:
        choice_user = choice_user.lower()
        print(f"Ok, you have chosen: {choice_user}.")
        break
'''

'''#input validation
if choice_user in array:
    print(f"Ok, you have chosen: {choice_user}.")
    #proceeds with the game
    heads_tails_game()
else:
    print("Please input a valid choice.")
    #loop it back to choice_user
'''