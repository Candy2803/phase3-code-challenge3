import sqlite3

# Connect to database
conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()

# Create bands table
cursor.execute('''
CREATE TABLE IF NOT EXISTS bands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL
);
''')

# Create venues table
cursor.execute('''
CREATE TABLE IF NOT EXISTS venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    city TEXT NOT NULL
);
''')

# Create concerts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS concerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    band_id INTEGER NOT NULL,
    venue_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (venue_id) REFERENCES venues(id)
);
''')

# Commit and close
conn.commit()
conn.close()

def insert_sample_data():
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    # Bands
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Westlife', 'Ireland')")
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Big Time Rush', 'USA')")
    
    # Venues
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Aviva Stadium', 'Ireland')")
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Madison Square Garden', 'New York')")
    
    # Concerts
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-10-28')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, '2024-09-29')")
    
    conn.commit()
    conn.close()

insert_sample_data()
