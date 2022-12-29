import sqlite3

# Create a connection
conn = sqlite3.connect('W5/todo.sqlite3')

# Cursor will allow user to execute sql statements
cur = conn.cursor()

# Create database using raw sql query
cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority INTEGER NOT NULL
    );
''')

# Insert a single record
cur.execute('''
    INSERT INTO tasks (title, description, priority)
    VALUES (?, ?, ?)
''', ('Quét nhà', '', 1)
)

# Insert multiple records
cur.executemany('''
    INSERT INTO tasks (title, description, priority)
    VALUES (?, ?, ?)
''', [('Học bài', '', 2), ('Đọc sách', '', 1)]
)

# Commit changes to database
conn.commit()

# Close connection after changes
conn.close()