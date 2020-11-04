import sqlite3

def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# Define Query
GET_CHARACTERS = """
    SELECT *
    FROM charactercreator_character;
"""

if __name__ == "__main__":
    # Connect to DB
    conn = connect_to_db()
    # Create Cursor
    curs = conn.cursor()
    # Execute Query
    results = execute_query(curs, GET_CHARACTERS)
    print(results[0])