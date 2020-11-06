SERVER = "lallah.db.elephantsql.com"
USERNAME = "mmapsmqx"
PASSWORD = "vSIvR5A4jnepdZ3ZqUjJiyFrkinRdO9q"

import psycopg2
import sqlite3

post = psycopg2.connect(host=SERVER,database=USERNAME,user=USERNAME,password=PASSWORD)
cursor = post.cursor()

lite = sqlite3.connect("../module1-introduction-to-sql/rpg_db.sqlite3")
liteCursor = lite.cursor()

QUERY = "SELECT * FROM charactercreator_character"

characters = liteCursor.execute(QUERY).fetchall()

# print(characters)

createTable = """
CREATE TABLE IF NOT EXISTS charactercreator_character (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
)
"""

cursor.execute(createTable)


for character in characters:
    query = f"""INSERT INTO charactercreator_character VALUES (
        {"%s, " * len(character[1:]) + '%s'}
    )"""
    cursor.execute(query, tuple(character))

cursor.close()
post.commit()