DROP TABLE IF EXISTS items;
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    done INTEGER NOT NULL
);