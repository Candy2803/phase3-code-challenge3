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

def get_band_for_concert(concert_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT bands.name, bands.hometown 
    FROM concerts 
    JOIN bands ON concerts.band_id = bands.id 
    WHERE concerts.id = ?;
    ''', (concert_id,))
    
    band = cursor.fetchone()
    conn.close()
    return band

def get_venue_for_concert(concert_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT venues.title, venues.city 
    FROM concerts 
    JOIN venues ON concerts.venue_id = venues.id 
    WHERE concerts.id = ?;
    ''', (concert_id,))
    
    venue = cursor.fetchone()
    conn.close()
    return venue

def get_concerts_for_venue(venue_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM concerts WHERE venue_id = ?;
    ''', (venue_id,))
    
    concerts = cursor.fetchall()
    conn.close()
    return concerts

def get_bands_for_venue(venue_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT DISTINCT bands.name 
    FROM concerts 
    JOIN bands ON concerts.band_id = bands.id 
    WHERE concerts.venue_id = ?;
    ''', (venue_id,))
    
    bands = cursor.fetchall()
    conn.close()
    return bands
