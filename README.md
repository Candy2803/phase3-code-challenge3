# Concerts Database Project

## Overview
This project is a concert booking system using SQLite, managing the relationships between `bands`, `venues`, and `concerts`. The database supports various operations like retrieving concert details, checking hometown performances, and identifying bands with the most shows.

This README is focused on setting up the project using **Visual Studio Code (VS Code)**.

## Prerequisites

Ensure you have the following installed:

- **Python 3.6+**
- **SQLite** (built-in with Python's `sqlite3` module)
- **Visual Studio Code** with:
  - **Python Extension** (`ms-python.python`)

### Install Python Extension in VS Code

1. Open **VS Code**.
2. Open the **Extensions** view (`Ctrl+Shift+X`).
3. Search for "Python" and install the extension by Microsoft.

## Project Setup

1. **Clone or Download** this project to your local machine.

2. Open the project in **Visual Studio Code**:
    - Click **File > Open Folder**, then select the project directory.

3. **Set Up the SQLite Database**:
    - The project uses `concerts.db`. To initialize it, run the `insert_sample_data()` function.

4. **Dependencies**:
    - Python’s built-in `sqlite3` is used, so no external libraries are required.

## How to Run

1. Open the terminal in VS Code:
    - Go to **Terminal > New Terminal** or press `Ctrl + ` (backtick).
  
2. Run the Python script:

    ```bash
    python your_script.py
    ```

    Replace `your_script.py` with the file name containing your project code.

## Code Overview

### Database Structure

- **bands**: Stores information about bands.
  
  ```sql
  CREATE TABLE bands (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      hometown TEXT NOT NULL
  );
