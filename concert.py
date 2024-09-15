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

# method to get band for concert
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

# method to get venue for concert
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

# method to get concerts for venue
def get_concerts_for_venue(venue_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM concerts WHERE venue_id = ?;
    ''', (venue_id,))
    
    concerts = cursor.fetchall()
    conn.close()
    return concerts

# method to get bands for venue
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

# method to get concert for band
def get_concerts_for_band(band_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM concerts WHERE band_id = ?;
    ''', (band_id,))
    
    concerts = cursor.fetchall()
    conn.close()
    return concerts

# method to get venue for band
def get_venues_for_band(band_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT DISTINCT venues.title 
    FROM concerts 
    JOIN venues ON concerts.venue_id = venues.id 
    WHERE concerts.band_id = ?;
    ''', (band_id,))
    
    venues = cursor.fetchall()
    conn.close()
    return venues

# method to validate hometown show
def is_hometown_show(concert_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT bands.hometown, venues.city 
    FROM concerts 
    JOIN bands ON concerts.band_id = bands.id 
    JOIN venues ON concerts.venue_id = venues.id 
    WHERE concerts.id = ?;
    ''', (concert_id,))
    
    hometown, city = cursor.fetchone()
    conn.close()
    return hometown == city

# method for concert introduction
def concert_introduction(concert_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT bands.name, bands.hometown, venues.city 
    FROM concerts 
    JOIN bands ON concerts.band_id = bands.id 
    JOIN venues ON concerts.venue_id = venues.id 
    WHERE concerts.id = ?;
    ''', (concert_id,))
    
    band_name, band_hometown, venue_city = cursor.fetchone()
    conn.close()
    print(f"We, the {band_name} from {band_hometown}, will be visiting {venue_city} soon!")

# method for play in venue
def play_in_venue(band_id, venue_id, date):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?);
    ''', (band_id, venue_id, date))
    
    conn.commit()
    conn.close()

# method for all introductions
def all_introductions(band_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT bands.name, bands.hometown, venues.city 
    FROM concerts 
    JOIN bands ON concerts.band_id = bands.id 
    JOIN venues ON concerts.venue_id = venues.id 
    WHERE bands.id = ?;
    ''', (band_id,))
    
    for band_name, band_hometown, venue_city in cursor.fetchall():
        print(f"We, the {band_name} from {band_hometown}, will be visiting {venue_city} soon!")
    
    conn.close()

# method for band with most performances
def band_with_most_performances():
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT bands.name, COUNT(concerts.id) AS num_concerts 
    FROM concerts 
    JOIN bands ON concerts.band_id = bands.id 
    GROUP BY bands.id 
    ORDER BY num_concerts DESC 
    LIMIT 1;
    ''')
    
    band = cursor.fetchone()
    conn.close()
    return band

# method for concert on date
def concert_on_date(venue_id, date):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM concerts 
    WHERE venue_id = ? AND date = ? 
    LIMIT 1;
    ''', (venue_id, date))
    
    concert = cursor.fetchone()
    conn.close()
    return concert

# method for most frequent band
def most_frequent_band(venue_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT bands.name, COUNT(concerts.id) AS num_concerts 
    FROM concerts 
    JOIN bands ON concerts.band_id = bands.id 
    WHERE concerts.venue_id = ? 
    GROUP BY bands.id 
    ORDER BY num_concerts DESC 
    LIMIT 1;
    ''', (venue_id,))
    
    band = cursor.fetchone()
    conn.close()
    return band
concert_introduction(1)  
all_introductions(1)  
