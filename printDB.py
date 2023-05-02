import sqlite3

# connect to the database
conn = sqlite3.connect('test_items.db')

# create a cursor object
cur = conn.cursor()

# execute a SELECT statement to fetch all rows from a table
cur.execute('SELECT * FROM items')

# fetch all rows and print them
rows = cur.fetchall()
for row in rows:
    print(row)

# close the cursor and the connection
cur.close()
conn.close()

def show_table_info(database, table):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("PRAGMA table_info({})".format(table))
    print(c.fetchall())
    conn.close()

show_table_info("test_items.db", "items")
