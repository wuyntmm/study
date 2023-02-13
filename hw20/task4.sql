CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    UNIQUE (first_name, last_name)
)
