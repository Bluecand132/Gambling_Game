
#checks if the username and password are in the database
def check_username_and_password():
    while True:
        username = input("Enter your username: ")
        #check to see if the username is in the database. if not, ask for username again

        #if the username is legit, check to see if the password is in the database. if not, ask for password again
        password = input("Enter your password: ")

#creates username and password
def create_username_and_password():
    print("If you ever want to go to the introduction, type 'Back' at any time.")
    while True:
        username = input("Enter a username: ")
        if username == 'Back':
            print("Ok, let's go back.")
            introduction()
            break
        else:
            password = get_password()
            confirm_password(password)
            break

def get_password():
    while True:
        password = input("Enter a password: ")
        if password == 'Back':
            print("Ok, let's go back.")
            introduction()
            break
        else:
            return password
            
#confirms password from user
def confirm_password(password):
    while True:
        password_confirmation = input("Confirm your password: ")
        if password_confirmation == 'Back':
            print("Ok, let's go back.")
            introduction()
            break
        elif password_confirmation == password:
            print("Ok, you have entered your username and password.")
            print("Let's put you in the database.")
            #put username and password in the user_table
            break
        else:
            print("The passwords do not match. Going back to sign in.")
            create_username_and_password()
            break



#introduction
def introduction():
    print("If you have a username or password, please enter number '1'.")
    print("Otherwise, please enter number '2'.")

    #chooses 1 or 2
    while True:
        try:
            if_user = int(input("Enter here: "))
            if if_user == 1:
                print ("Ok, let's check your username and password.")
                check_username_and_password()
                break
            elif if_user == 2:
                print("Ok, let's create you a username and password.")
                create_username_and_password()
                break
            else:
                print("The input you entered is not valid. Please try again.")
        except ValueError:
            print("The input you entered is not valid. Please try again.")
            continue

#creates username and password
# def create_username_and_password():
#     print("If you ever want to go to the introduction, type 'Back' at any time.")
#     while True:
#         username = input("Enter a username: ")
#         if username == 'Back':
#             print("Ok, let's go back.")
#             introduction()
#             break
#         else:
#             while True:
#                 while True:
#                     password = input("Enter a password: ")
#                     if password == 'Back':
#                         print("Ok, let's go back.")
#                         introduction()
#                         break
#                     else:
#                         password_confirmation = input("Confirm your password: ")
#                         # if password == password_confirmation:
#                         #     print("Ok, you have entered your username and password.")
#                         #     print("Let's put you in the database.")
#                         #     #put username and password in the user_table
#                         #     break
#                         if password_confirmation == 'Back':
#                             print("Ok, let's go back.")
#                             introduction()
#                             break
#                         elif password == password_confirmation:
#                             print("Ok, you have entered your username and password.")
#                             print("Let's put you in the database.")
#                             #put username and password in the user_table
#                             break
#                         else:
#                             print("The passwords do not match. Please try again.")
#                             continue

print("Hello! Welcome to this awesome gambling game!")
introduction()
