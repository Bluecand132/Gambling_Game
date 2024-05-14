import sqlite3
import bcrypt
import keyflow as kfprint

username = "test"
connection = sqlite3.connect('user_database.db')
cursor = connection.cursor()

username_id_array = cursor.execute("SELECT id FROM user_table WHERE username = ?", (username,))
username_id = cursor.fetchone()[0]
stats_array = cursor.execute("SELECT * FROM score_table WHERE id = ?", (username_id,))
stats = cursor.fetchone()
print(f"\nBalance: {stats[1]}\nWins: {stats[2]}\nLosses: {stats[3]}\nDraws: {stats[4]}\nAverage Wins: {stats[5]}\nAverage Losses: {stats[6]}\n Average Draws: {stats[7]}")