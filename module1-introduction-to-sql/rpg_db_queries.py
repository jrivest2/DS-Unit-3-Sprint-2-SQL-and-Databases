# How many total Characters are there?
char_num = """
    SELECT COUNT(*)
    FROM charactercreator_character;
"""
# Answer: 302


# How many of each specific subclass?
num_nec = """
    SELECT COUNT(*)
    FROM charactercreator_necromancer;
"""
# Answer: 11

# How many total Items?
num_items = """
    SELECT COUNT(*)
    FROM armory_item;
"""
# Answer: 174

# How many of the Items are weapons? How many are not?
num_weapons = """
    SELECT COUNT(*)
    FROM armory_weapon;
"""
num_nonWeapons = """
  SELECT
    ((SELECT COUNT(*)
    FROM armory_item)
    -
    (SELECT COUNT(*)
    FROM armory_weapon));
"""
# Answer Weapons: 37
# Answer Non-weapons: 137

# How many Items does each character have? (Return first 20 rows)
items_per_char = """
    SELECT ccc.name,ccc.character_id,cci.item_id, COUNT(cci.item_id) AS Count
    FROM charactercreator_character AS ccc
    LEFT JOIN charactercreator_character_inventory AS cci
    on ccc.character_id = cci.character_id
    GROUP BY ccc.character_id
    LIMIT 20;
"""


# How many Weapons does each character have? (Return first 20 rows)
weapons_per_char = """
    SELECT ccc.name,ccc.character_id,cci.item_id, COUNT(cci.item_id) AS Count
    FROM charactercreator_character AS ccc
    LEFT JOIN charactercreator_character_inventory AS cci
    on ccc.character_id = cci.character_id
    INNER JOIN armory_weapon AS aw
    on cci.item_id == aw.item_ptr_id
    GROUP BY ccc.character_id
    LIMIT 20;
"""


# On average, how many Items does each Character have?
avg_items_per_char = """    
    CREATE TABLE items_per_char AS
    SELECT ccc.name,ccc.character_id,cci.item_id, COUNT(cci.item_id) AS Count
    FROM charactercreator_character AS ccc
    LEFT JOIN charactercreator_character_inventory AS cci
    on ccc.character_id = cci.character_id
    GROUP BY ccc.character_id;
    SELECT AVG(Count)
    FROM items_per_char;
"""


# On average, how many Weapons does each character have?
avg_weapons_per_char = """
    CREATE TABLE weapons_per_char AS
    SELECT ccc.name,ccc.character_id,cci.item_id, COUNT(cci.item_id) AS Count
    FROM charactercreator_character AS ccc
    LEFT JOIN charactercreator_character_inventory AS cci
    on ccc.character_id = cci.character_id

    INNER JOIN armory_weapon AS aw
    on cci.item_id == aw.item_ptr_id
    GROUP BY ccc.character_id;
    SELECT AVG(Count)
    FROM weapons_per_char;
"""
