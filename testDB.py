import sqlite3

conn = sqlite3.connect('test_items.db')
c = conn.cursor()
#
c.execute('''DROP TABLE IF EXISTS items;''')

# Create table
c.execute('''CREATE TABLE items
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, done INTEGER NOT NULL)''')

# Insert some test data
c.execute("INSERT INTO items (name, done) VALUES (?, ?)", ('Buy milk', False))
c.execute("INSERT INTO items (name, done) VALUES (?, ?)", ('Walk the dog', False))
c.execute("INSERT INTO items (name, done) VALUES (?, ?)", ('Take out the trash', False))

# Commit changes and close the connection
conn.commit()
conn.close()


