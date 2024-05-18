import sqlite3

username = "encrypt"

def average_stats(stats):
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()

    total = stats[2] + stats[3] + stats[4]
    a_wins = stats[2] / total
    a_losses = stats[3] / total
    a_draws = stats[4] / total

    cursor.execute("UPDATE score_table SET avg_wins = ? WHERE id = ?", (a_wins, stats[0]))
    cursor.execute("UPDATE score_table SET avg_losses = ? WHERE id = ?", (a_losses, stats[0]))
    cursor.execute("UPDATE score_table SET avg_draws = ? WHERE id = ?", (a_draws, stats[0]))

    connection.commit()
    cursor.close()
    connection.close()

average_stats(username)