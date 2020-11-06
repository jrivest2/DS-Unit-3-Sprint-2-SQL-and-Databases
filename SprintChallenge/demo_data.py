import sqlite3
# PART 1
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


# drop table if you've run this code before
curs.execute('DROP TABLE IF EXISTS demo;')
conn.commit()


# Create the table
create_table = """
CREATE TABLE IF NOT EXISTS demo(
    s TEXT,
    x INT,
    y INT
);
"""

curs.execute(create_table)
conn.commit()

# Insert data into the table
s = ['g','v','f']
x = [3,5,8]
y = [9,7,7]
for i in range(len(s)):
        
    insert_data = f"""
    INSERT INTO demo VALUES(
            {"'"+s[i]+"'"},
            {x[i]},
            {y[i]}
        );
    """
    curs.execute(insert_data)
    conn.commit()

# Function to handle queries
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# Test to make sure the table got built correctly
query0 = """
SELECT *
FROM demo;
"""
print(execute_query(curs, query0))

# Count how many rows (Should be 3)
query1 = """
SELECT COUNT(s)
FROM demo;
"""
print(execute_query(curs,query1)[0][0])

# How many rows are there where both x and y are at least 5
query2 = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5 AND y >= 5;
"""
print(execute_query(curs,query2)[0][0])

# How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
# `DISTINCT`)?
query3 = """
SELECT COUNT(DISTINCT y)
FROM demo;
"""
print(execute_query(curs,query3)[0][0])