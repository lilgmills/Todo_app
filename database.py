import sqlite3

current_todo_id = 1

def create_schema(dbase):
    # Connect to the database
    conn = sqlite3.connect(dbase)
    c = conn.cursor()

    # Drop existing tables if they exist and create new tables
    c.execute('''DROP TABLE IF EXISTS todo_lists''')
    c.execute('''CREATE TABLE todo_lists
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL)''')

    c.execute('''DROP TABLE IF EXISTS items;''')
    c.execute('''CREATE TABLE items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                done INTEGER DEFAULT 0,
                todo_list_id INTEGER NOT NULL,
                FOREIGN KEY (todo_list_id) REFERENCES todo_lists(id))''')

    # Insert a default todo list if it doesn't exist
    c.execute('''INSERT INTO todo_lists (name) 
                 SELECT 'Todo List' 
                 WHERE NOT EXISTS (SELECT * FROM todo_lists)''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def get_items(dbase, current_todo_id):
 
    conn = sqlite3.connect(dbase)
    c = conn.cursor()

    # Retrieve items for the given todo list id
    query = f"SELECT * FROM items WHERE todo_list_id = ?"
    c.execute(query, (current_todo_id,))
    items = c.fetchall()

    # Close the connection and return the items
    conn.close()
    return items

def get_todo_lists(dbase):
  
    conn = sqlite3.connect(dbase)
    c = conn.cursor()

    # Retrieve all todo lists
    query = f"SELECT * FROM todo_lists"
    c.execute(query)
    todo_lists = c.fetchall()

    # Close the connection and return the todo lists
    conn.close()
    return todo_lists

def get_current_list_name(dbase, current_todo_id):
  
    conn = sqlite3.connect(dbase)
    c = conn.cursor()

    # Retrieve the name of the current todo list
    query = f"SELECT name FROM todo_lists WHERE id = ?"
    c.execute(query, (current_todo_id,))
    current_list_name = c.fetchall()

    # Close the connection and return the current list name
    conn.close()
    for row in current_list_name:
        for name in row:
            return name

def add_task(dbase, new_item, current_todo_id):
   
    conn = sqlite3.connect(dbase)
    c = conn.cursor()

    # Add a new task to the items table
    c.execute("INSERT INTO items (name, done, todo_list_id) VALUES (?, ?, ?)", (new_item, False, current_todo_id))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def update_list_name(dbase, todo_list_id, new_name):
   
    conn = sqlite3.connect(dbase)
    c = conn.cursor()

    # Update the name of a todo list
    query = "UPDATE todo_lists SET name = ? WHERE id = ?"
    c.execute(query, (new_name, todo_list_id,))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def update_completed_task(dbase, item_id, done_int):
    
    conn = sqlite3.connect(dbase)
    c = conn.cursor()

    # Update the completed status of a task
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


