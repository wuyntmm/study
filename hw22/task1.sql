CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);

CREATE TABLE IF NOT EXISTS publishing_house(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name TEXT,
    rating INTEGER DEFAULT 5
);

CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    title TEXT,
    author TEXT,
    year INTEGER,
    price INTEGER,
    publishing_house_id INTEGER,
    FOREIGN KEY (publishing_house_id) REFERENCES publishing_house(id)
);

CREATE TABLE IF NOT EXISTS purchases(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    user_id INTEGER,
    book_id INTEGER,
    date TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
)