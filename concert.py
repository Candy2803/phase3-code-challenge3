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

    def insert_sample_data(self):
        # Insert sample data
        self.cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Westlife', 'Ireland')")
        self.cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Big Time Rush', 'USA')")
        self.cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Maverick City', 'UK')")

        self.cursor.execute("INSERT INTO venues (title, city) VALUES ('Aviva Stadium', 'Ireland')")
        self.cursor.execute("INSERT INTO venues (title, city) VALUES ('Madison Square Garden', 'New York')")
        self.cursor.execute("INSERT INTO venues (title, city) VALUES ('Maverick City', 'UK')")

        self.cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-10-28')")
        self.cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, '2024-09-29')")
        self.cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (3, 3, '2024-11-05')")

        self.conn.commit()

    def close(self):
        self.conn.close()


class Band:
    def __init__(self, db: ConcertDatabase):
        self.db = db
# method to get band for concert
    def get_band_for_concert(self, concert_id):
        self.db.cursor.execute('''
        SELECT bands.name, bands.hometown 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        WHERE concerts.id = ?;
        ''', (concert_id,))
        return self.db.cursor.fetchone()
# method to get concerts for band
    def get_concerts_for_band(self, band_id):
        self.db.cursor.execute('''
        SELECT * FROM concerts WHERE band_id = ?;
        ''', (band_id,))
        return self.db.cursor.fetchall()
# method to get venues for band
    def get_venues_for_band(self, band_id):
        self.db.cursor.execute('''
        SELECT DISTINCT venues.title 
        FROM concerts 
        JOIN venues ON concerts.venue_id = venues.id 
        WHERE concerts.band_id = ?;
        ''', (band_id,))
        return self.db.cursor.fetchall()
# method to get bands with most performances
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
    def __init__(self, db: ConcertDatabase):
        self.db = db
# method to get venue for concert
    def get_venue_for_concert(self, concert_id):
        self.db.cursor.execute('''
        SELECT venues.title, venues.city 
        FROM concerts 
        JOIN venues ON concerts.venue_id = venues.id 
        WHERE concerts.id = ?;
        ''', (concert_id,))
        return self.db.cursor.fetchone()
# method to get concert for venue
    def get_concerts_for_venue(self, venue_id):
        self.db.cursor.execute('''
        SELECT * FROM concerts WHERE venue_id = ?;
        ''', (venue_id,))
        return self.db.cursor.fetchall()
# method to get bands for venue
    def get_bands_for_venue(self, venue_id):
        self.db.cursor.execute('''
        SELECT DISTINCT bands.name 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        WHERE concerts.venue_id = ?;
        ''', (venue_id,))
        return self.db.cursor.fetchall()
# method to get most frequent band
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
    def __init__(self, db: ConcertDatabase):
        self.db = db
# method to see whether it is a home town show
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

    def all_introductions(self, band_id):
        self.db.cursor.execute('''
        SELECT DISTINCT bands.name, bands.hometown, venues.city
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE bands.id = ?
        LIMIT 1;
        ''', (band_id,))
        band_name, band_hometown, venue_city = self.db.cursor.fetchone()
        print(f"We, the {band_name} from {band_hometown}, will be visiting {venue_city} soon!")


db = ConcertDatabase()
db.create_tables()
db.insert_sample_data()

band = Band(db)
venue = Venue(db)
concert = Concert(db)

concert.concert_introduction(1)  
all_bands = band.band_with_most_performances() 
print("Band with the most performances:", all_bands)
db.close()
