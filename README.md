<<<<<<< HEAD
# Mock-Code-Challenge---Concerts

# Concert Management System

This project is a concert management system built using Python and SQLite3. It allows users to manage bands, venues, and concerts by tracking information such as performances and hometown shows. The system enables the creation, retrieval, and querying of concert details while managing the relationships between bands, venues, and concert data.
Features

    1. Bands Table: Stores information about bands, including their name and hometown.
    2. Venues Table: Stores venue details, including the title and city.
    3. Concerts Table: Tracks concerts by linking bands and venues along with the concert date.
    4. Concert Operations: Provides methods to retrieve concert information, including band and venue details, hometown shows, and concert introductions.
    5. Venue Operations: Includes methods to list concerts at specific venues, retrieve bands that have performed at a venue, and find concerts on specific dates.
    6. Band Operations: Lists all concerts for a specific band, retrieves venues they have performed at, creates new concerts, and generates concert introductions.
    7. Query Methods: Finds the band with the most performances and the most frequent band at a venue.

## Database Structure

The system uses three SQLite tables:

    bands
        id: Integer (Primary Key)
        name: Text (Band name)
        hometown: Text (Band's hometown)

    venues
        id: Integer (Primary Key)
        title: Text (Venue title)
        city: Text (Venue city)

    concerts
        id: Integer (Primary Key)
        band_id: Integer (Foreign Key referencing bands)
        venue_id: Integer (Foreign Key referencing venues)
        date: Text (Concert date)

## Setup Instructions

    Clone the repository:

    
1. git clone https://github.com/Anthony-Maundu/Mock-Code-Challenge---Concerts.git

2. Navigate to the project directory:

cd Mock-Code-Challenge---Concerts

3. Install Dependencies: Ensure you have Python and SQLite3 installed on your system.

4. Run the Code: Use the following command to run the script:

    python3 concerts.py

## Functions and Methods
1. Concert Functions

    get_band_for_concert(concert_id): Returns the band instance for a specific concert.
    get_venue_for_concert(concert_id): Returns the venue instance for a specific concert.
    is_hometown_show(concert_id): Returns True if the concert is in the band's hometown, False otherwise.
    concert_introduction(concert_id): Returns a formatted string introducing the band at the concert.

2. Band Functions

    get_concerts_for_band(band_id): Returns all concerts for a specific band.
    get_venues_for_band(band_id): Returns all venues where the band has performed.
    play_in_venue(band_id, venue_id, date): Creates a new concert entry for a band at a venue.
    all_introductions(band_id): Returns all concert introductions for a band.
    band_with_most_performances(): Returns the band with the most performances.

3. Venue Functions

    get_concerts_for_venue(venue_id): Returns all concerts for a specific venue.
    get_bands_for_venue(venue_id): Returns all bands that have performed at a venue.
    concert_on_date(venue_id, date): Finds the first concert at a venue on a specific date.
    most_frequent_band(venue_id): Returns the band that has performed the most at a venue.

## Sample Data

The insert_sample_data() function populates the database with the following records:

    Bands: Example bands such as Sauti-Sol and Wakadinali.
    Venues: Example venues like Kasarani Stadium and Carnivore Gardens.
    Concerts: Example concert dates, band performances, and venue locations.

## Credits

This project was created and maintained by Anthony Maundu.
=======
# 🎸 Concert Management System

Welcome to the **Concert Management System**! This project is a Python-based application designed to manage bands, venues, and concerts. With SQLite as the database, the system allows users to perform various operations such as tracking concert performances, managing venue bookings, and exploring band performance history.

## 📋 Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Classes](#classes)

---

## 🚀 Features

- **Bands**: Add bands, view their concert schedules, and manage performances.
- **Venues**: Manage venue bookings, explore upcoming concerts, and track band performances at specific venues.
- **Concerts**: Schedule concerts, track band-venue relationships, and check if concerts are hometown shows.
- **Statistics**: View interesting statistics like the band with the most performances or the most frequent band at a venue.

---

## 🛠️ Setup

### Prerequisites:
- Python 3.x
- SQLite (No additional setup required as it's bundled with Python)

### Steps to Set Up:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Candy2803/phase3-code-challenge3
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd concert-management
   ```

3. **Install the required packages** (if any):
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the project**:
   ```bash
   python main.py
   ```

---

## 🎯 Usage

### Sample Operations:

1. **Add Sample Data**: Automatically create sample bands, venues, and concerts by running the seed script:
   ```bash
   python seed.py
   ```

2. **Explore Concerts**: Use the `Concert` class to display upcoming concerts and manage new bookings.
   ```python
   concert = Concert(db)
   concert.concert_introduction(1)  # Introduces a specific concert
   ```

3. **Get Band Information**: Find out which band has the most performances or check the schedule for a specific band.
   ```python
   band = Band(db)
   print(band.band_with_most_performances())
   ```

4. **Manage Venues**: List the concerts taking place at a specific venue or find the band that plays most frequently at the venue.
   ```python
   venue = Venue(db)
   print(venue.most_frequent_band(1))
   ```

---

## 🗂️ Database Schema

The system uses an SQLite database (`concerts.db`) with three main tables:

- **bands**: Stores band details.
- **venues**: Stores venue details.
- **concerts**: Stores the relationships between bands, venues, and concert dates.

### Tables Overview:
- **bands**
  - `id` (integer, primary key)
  - `name` (text, not null)
  - `hometown` (text, not null)

- **venues**
  - `id` (integer, primary key)
  - `title` (text, not null)
  - `city` (text, not null)

- **concerts**
  - `id` (integer, primary key)
  - `band_id` (integer, foreign key from `bands`)
  - `venue_id` (integer, foreign key from `venues`)
  - `date` (text, not null)

---

## 🏛️ Classes

The project is organized around the following classes, each of which represents a different part of the system:

- **ConcertDatabase**: Handles the creation of tables and general database management.
- **Band**: Contains methods to manage and retrieve information related to bands.
- **Venue**: Manages venue operations and handles queries related to venues.
- **Concert**: Manages concert-related operations, like checking if a concert is a hometown show or scheduling a new concert.

---

Made with ❤️ by Candy Wawuda Mzungu.

---
>>>>>>> 9b659d1 (committed)
