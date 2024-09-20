from concert import ConcertDatabase

def insert_sample_data(db):
    # Insert sample bands
    db.cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Westlife', 'Ireland')")
    db.cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Big Time Rush', 'USA')")
    db.cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Maverick City', 'UK')")

    # Insert sample venues
    db.cursor.execute("INSERT INTO venues (title, city) VALUES ('Aviva Stadium', 'Ireland')")
    db.cursor.execute("INSERT INTO venues (title, city) VALUES ('Madison Square Garden', 'New York')")
    db.cursor.execute("INSERT INTO venues (title, city) VALUES ('Wembley Stadium', 'London')")

    # Insert sample concerts
    db.cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-10-28')")
    db.cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, '2024-09-29')")
    db.cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (3, 3, '2024-11-05')")

    db.conn.commit()

if __name__ == "__main__":
    db = ConcertDatabase()
    db.create_tables()
    insert_sample_data(db)
    db.close()
