import socket
import pyModeS as pms

HOST = 'localhost'  # IP address or hostname where dump1090 is running
PORT = 30002        # The default dump1090 SBS-1 output port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024).decode('utf-8')
        if data:
            # Parse ADS-B message
            msg = pms.parsing.df(data.strip())
            if msg:
                # Extract relevant data from the parsed message
                icao24 = msg[0]
                lat = msg[14]
                lon = msg[15]
                altitude = msg[11]

                # Insert data into the database
                cursor.execute('''
                    INSERT INTO aircraft_position (ICAO24, Latitude, Longitude, Altitude, Timestamp)
                    VALUES (?, ?, ?, ?, datetime('now'))
                ''', (icao24, lat, lon, altitude))
                conn.commit()

