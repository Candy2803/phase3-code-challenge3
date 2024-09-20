from concert import ConcertDatabase, Band, Venue, Concert

def main():
    # Initialize database connection
    db = ConcertDatabase()
    db.create_tables()  # Ensure tables exist

    # Example usage
    # You need to provide relevant attributes for band, venue, and concert

    # Creating dummy band and venue just for demonstration
    band = Band(name="Sample Band", hometown="Sample Town", db=db)
    venue = Venue(title="Sample Venue", city="Sample City", db=db)
    concert = Concert(band_id=1, venue_id=1, db=db)

    # For existing concerts in the database
    try:
        concert.concert_introduction(1)  # Assuming there's a concert with ID 1
    except TypeError:
        print("Concert not found or missing data.")
    
    # Query the band with the most performances
    most_performances_band = band.band_with_most_performances()
    print("Band with the most performances:", most_performances_band)

    # Close database connection
    db.close()

if __name__ == "__main__":
    main()
