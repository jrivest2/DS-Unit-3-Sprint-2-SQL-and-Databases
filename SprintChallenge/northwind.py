import sqlite3

# connect to the database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Function to handle queries
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# What are the ten most expensive items (per unit price) in the database?
query1 = """
SELECT Id, ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""
print(execute_query(curs,query1))

# What is the average age of an employee at the time of their hiring? (Hint: a
# lot of arithmetic works with dates.)

query2 = """
SELECT((SELECT AVG(HireDate)
         FROM Employee)
         -
        (SELECT AVG(BirthDate)
         FROM Employee));
"""
print(execute_query(curs,query2)[0][0])

# STRETCH GOAL
# How does the average age of employee at hire vary by city?