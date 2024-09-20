import sqlite3

class ConcertDatabase:
    def __init__(self, db_name='concerts.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # Create bands table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hometown TEXT NOT NULL
        );
        ''')

        # Create venues table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            city TEXT NOT NULL
        );
        ''')

        # Create concerts table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            band_id INTEGER NOT NULL,
            venue_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (band_id) REFERENCES bands(id),
            FOREIGN KEY (venue_id) REFERENCES venues(id)
        );
        ''')

        self.conn.commit()

    def close(self):
        self.conn.close()


class Band:
    def __init__(self, name, hometown, db: ConcertDatabase):
        self.name = name
        self.hometown = hometown
        self.db = db

    def get_band_for_concert(self, concert_id):
        self.db.cursor.execute('''
        SELECT bands.name, bands.hometown 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        WHERE concerts.id = ?;
        ''', (concert_id,))
        return self.db.cursor.fetchone()

    def get_concerts_for_band(self, band_id):
        self.db.cursor.execute('''
        SELECT * FROM concerts WHERE band_id = ?;
        ''', (band_id,))
        return self.db.cursor.fetchall()

    def get_venues_for_band(self, band_id):
        self.db.cursor.execute('''
        SELECT DISTINCT venues.title 
        FROM concerts 
        JOIN venues ON concerts.venue_id = venues.id 
        WHERE concerts.band_id = ?;
        ''', (band_id,))
        return self.db.cursor.fetchall()

    def band_with_most_performances(self):
        self.db.cursor.execute('''
        SELECT bands.name, COUNT(concerts.id) AS num_concerts 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        GROUP BY bands.id 
        ORDER BY num_concerts DESC 
        LIMIT 1;
        ''')
        return self.db.cursor.fetchone()


class Venue:
    def __init__(self, title, city, db: ConcertDatabase):
        self.title = title
        self.city = city
        self.db = db

    def get_venue_for_concert(self, concert_id):
        self.db.cursor.execute('''
        SELECT venues.title, venues.city 
        FROM concerts 
        JOIN venues ON concerts.venue_id = venues.id 
        WHERE concerts.id = ?;
        ''', (concert_id,))
        return self.db.cursor.fetchone()

    def get_concerts_for_venue(self, venue_id):
        self.db.cursor.execute('''
        SELECT * FROM concerts WHERE venue_id = ?;
        ''', (venue_id,))
        return self.db.cursor.fetchall()

    def get_bands_for_venue(self, venue_id):
        self.db.cursor.execute('''
        SELECT DISTINCT bands.name 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        WHERE concerts.venue_id = ?;
        ''', (venue_id,))
        return self.db.cursor.fetchall()

    def most_frequent_band(self, venue_id):
        self.db.cursor.execute('''
        SELECT bands.name, COUNT(concerts.id) AS num_concerts 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        WHERE concerts.venue_id = ? 
        GROUP BY bands.id 
        ORDER BY num_concerts DESC 
        LIMIT 1;
        ''', (venue_id,))
        return self.db.cursor.fetchone()


class Concert:
    def __init__(self, band_id, venue_id, db: ConcertDatabase):
        self.band_id = band_id
        self.venue_id = venue_id
        self.db = db

    def is_hometown_show(self, concert_id):
        self.db.cursor.execute('''
        SELECT bands.hometown, venues.city 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        JOIN venues ON concerts.venue_id = venues.id 
        WHERE concerts.id = ?;
        ''', (concert_id,))
        hometown, city = self.db.cursor.fetchone()
        return hometown == city

    def play_in_venue(self, band_id, venue_id, date):
        self.db.cursor.execute('''
        INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?);
        ''', (band_id, venue_id, date))
        self.db.conn.commit()

    def concert_on_date(self, venue_id, date):
        self.db.cursor.execute('''
        SELECT * FROM concerts 
        WHERE venue_id = ? AND date = ? 
        LIMIT 1;
        ''', (venue_id, date))
        return self.db.cursor.fetchone()

    def concert_introduction(self, concert_id):
        self.db.cursor.execute('''
        SELECT bands.name, bands.hometown, venues.city 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        JOIN venues ON concerts.venue_id = venues.id 
        WHERE concerts.id = ?;
        ''', (concert_id,))
        band_name, band_hometown, venue_city = self.db.cursor.fetchone()
        print(f"We, the {band_name} from {band_hometown}, will be visiting {venue_city} soon!")
