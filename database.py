import sqlite3

def create_todo_table(dbase):
    conn = sqlite3.connect(dbase)
    c = conn.cursor()
    #c.execute('''DROP TABLE IF EXISTS items''')
    c.execute('''CREATE TABLE IF NOT EXISTS items
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 done INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

def get_items(dbase):
    conn = sqlite3.connect(dbase)
    c = conn.cursor()
    query = f"SELECT * FROM items"
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return items

def add_task(dbase, new_item):
    conn = sqlite3.connect(dbase)
    c = conn.cursor()
    c.execute("INSERT INTO items (name, done) VALUES (?, ?)", (new_item, False))
    conn.commit()
    conn.close()

def update_completed_task(dbase, item_id, done_int):
    conn = sqlite3.connect(dbase)
    c = conn.cursor()
    c.execute("UPDATE items SET done = ? WHERE id = ?", (done_int, item_id,))
    conn.commit()
    conn.close()

def edit_task(dbase, item_id, new_text):
    conn = sqlite3.connect(dbase)
    c = conn.cursor()
    c.execute("UPDATE items SET name = ? WHERE id = ?", (new_text, item_id,))
    conn.commit()
    conn.close()

def delete_task(dbase, item_id):
    conn = sqlite3.connect(dbase)
    c = conn.cursor()
    c.execute("DELETE FROM items WHERE id=?", (item_id,))
    conn.commit()
    conn.close()

def get_db_connection(dbase):
    conn = sqlite3.connect(dbase)
    conn.row_factory = sqlite3.Row
    return conn


