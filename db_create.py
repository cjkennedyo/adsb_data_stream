import sqlite3

# Connect to the SQLite database (or use another database of your choice)
conn = sqlite3.connect('adsb_data.db')
cursor = conn.cursor()

# Create a table to store positional data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS aircraft_position (
        ICAO24 TEXT,
        Latitude REAL,
        Longitude REAL,
        Altitude INT,
        Timestamp DATETIME
    )
''')
conn.commit()

