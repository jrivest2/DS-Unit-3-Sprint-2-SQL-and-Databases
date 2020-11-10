import sqlite3

# PART 2
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

# Output:
"""
[(38, 'Côte de Blaye', 263.5),
 (29, 'Thüringer Rostbratwurst', 123.79),
 (9, 'Mishi Kobe Niku', 97),
 (20, "Sir Rodney's Marmalade", 81),
 (18, 'Carnarvon Tigers', 62.5),
 (59, 'Raclette Courdavault', 55),
 (51, 'Manjimup Dried Apples', 53), 
 (62, 'Tarte au sucre', 49.3), 
 (43, 'Ipoh Coffee', 46), 
 (28, 'Rössle Sauerkraut', 45.6)]
"""

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

# Output:
"""
37.22222222222217
"""

# PART 3

# What are the ten most expensive items (per unit price) in the
#  database *and* their suppliers?

query3 = """
SELECT Product.Id, Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
LEFT JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;
"""
print(execute_query(curs,query3))

# Output:
"""
[(38, 'Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'), 
(29, 'Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'), 
(9, 'Mishi Kobe Niku', 97, 'Tokyo Traders'), 
(20, "Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'), 
(18, 'Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'), 
(59, 'Raclette Courdavault', 55, 'Gai pâturage'), 
(51, 'Manjimup Dried Apples', 53, "G'day, Mate"), 
(62, 'Tarte au sucre', 49.3, "Forêts d'érables"), 
(43, 'Ipoh Coffee', 46, 'Leka Trading'), 
(28, 'Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]
"""

# What is the largest category (by number of unique products in it)?
query4 = """
SELECT Category.CategoryName, COUNT(*)
FROM Product
LEFT JOIN Category
ON Product.CategoryId = Category.Id
Group BY Category.CategoryName
ORDER BY COUNT(*) DESC
LIMIT 1;
"""
print(execute_query(curs,query4))

# Output:
"""
[('Confections', 13)]
"""