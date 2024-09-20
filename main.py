from concert import ConcertDatabase, Band, Venue, Concert

def main():
    db = ConcertDatabase()
    band = Band(db)
    venue = Venue(db)
    concert = Concert(db)

    # Example usage
    concert.concert_introduction(1)
    most_performances_band = band.band_with_most_performances()
    print("Band with the most performances:", most_performances_band)

    db.close()

if __name__ == "__main__":
    main()
