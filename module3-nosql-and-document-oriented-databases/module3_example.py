"""An example of how to import the character table into MongoDB from SQLite"""

# "How was working with MongoDB different from working with
#   PostgreSQL? What was easier, and what was harder?"
# Answer: MongoDB was easier.
import sqlite3
import pymongo

PASSWORD = "eJHXOMYXtZsX2JhB"
DBNAME = "test"

def create_mdb_connection(password,dbname):
    client = pymongo.MongoClient("mongodb+srv://jrivest2:{}@cluster0.aonzs.mongodb.net/{}?retryWrites=true&w=majority".format(password,dbname))
    return client

def creat_sl_conn(extraction_db="../DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3"):
    sl_conn = sqlite3.connect(extraction_db)
    return sl_conn

def execute_query(curs, query):
    return curs.execute(query).fetchall()

def char_doc_creation(mongo_db, characters):
    # character - {id, name, level, exp, hp, strength, intelligence, dexterity, wisdom}
    for character in characters:
        character_doc ={
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "widsom": character[8]
        }
        mongo_db.test.insert_one(character_doc)


GET_CHARACTERS = "SELECT * FROM charactercreator_character"



if __name__ == "__main__":
    sl_conn = creat_sl_conn()
    sl_curs = sl_conn.cursor()
    client = create_mdb_connection(PASSWORD,DBNAME)
    db = client.test
    characters = execute_query(sl_curs, GET_CHARACTERS) # Should return a list
    char_doc_creation(db,characters)