import sqlite3
import bcrypt
import keyflow as kfprint

check_password = input("Enter password to check: ")

connection = sqlite3.connect('user_database.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM user_table WHERE password = ?", (check_password,))
hashed_password_from_database = cursor.fetchone()

# Check if password exists in the database
if hashed_password_from_database is not None:
    # Check if password matches the hashed password in the database
    if bcrypt.checkpw(check_password.encode('utf-8'), hashed_password_from_database[1]):
        print("Password matches!")
    else:
        print("Password does not match!")
else:
    print("Sorry, this password doesn't exist.")
    print("Try again.")