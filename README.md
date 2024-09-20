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

