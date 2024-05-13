import sqlite3

#define connection (used to connect to a database) and cursor (used to interact with the database(e.g manupulate it))
connection = sqlite3.connect('user_database.db')
cursor = connection.cursor()

#creates user_table

# create_table_sql = '''
# CREATE TABLE IF NOT EXISTS user_table (
# 		id INTEGER PRIMARY KEY,
# 		username TEXT,
# 		password TEXT
# 	);
# '''

# cursor.execute(create_table_sql)

# id_test = 1
# username = 'orangesidny'
# password = 'ILovePython123!'

# #inserts the data in the database
# INSERT_QUERY = "INSERT INTO user_table (id, username, password) VALUES (?, ?, ?)"
# cursor.execute(INSERT_QUERY, (id_test, username, password))


# #saves changes made
# connection.commit()

# #closes cursor
# cursor.close()

# #closes connection
# connection.close()

#creates score_table
# create_table_sql = '''
#     CREATE TABLE IF NOT EXISTS score_table (
#     id INTEGER PRIMARY KEY,
#     balance INTEGER,
#     wins INTEGER,
#     losses INTEGER,
#     draws INTEGER,
#     avg_wins INTEGER,
#     avg_losses INTEGER,
#     avg_draws INTEGER
#     );
# '''

# cursor.execute(create_table_sql)

# id_foreign_test = 1
# balance_test = 50.00
# wins_test = 6
# losses_test = 9
# draws_test = 0
# avg_wins_test = wins_test/(wins_test + losses_test + draws_test)
# avg_losses_test = losses_test/(wins_test + losses_test + draws_test)
# avg_draws_test = draws_test/(wins_test + losses_test + draws_test)

# INSERT_QUERY = "INSERT INTO score_table (id, balance, wins, losses, draws, avg_wins, avg_losses, avg_draws) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
# cursor.execute(INSERT_QUERY, (id_foreign_test, balance_test, wins_test, losses_test, draws_test, avg_wins_test, avg_losses_test, avg_draws_test))

# #saves changes made
# connection.commit()

# #closes cursor
# cursor.close()

# #closes connection
# connection.close()

salt = '''
    ALTER TABLE user_table ADD COLUMN salt;
'''

cursor.execute(salt)