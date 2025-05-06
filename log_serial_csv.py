# Python serial logger

import serial
import csv
from datetime import datetime

# Setup serial connection (adjust port as needed)
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Open CSV file for appending data
with open('sensor_data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Timestamp', 'Temperature (°C)', 'Humidity (%)'])  # Header

    while True:
        try:
            line = ser.readline().decode().strip()
            parts = line.split(',')
            if len(parts) == 2:
                temp = float(parts[0])
                humidity = float(parts[1])
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([timestamp, temp, humidity])
                print(f"Logged: {timestamp}, Temp: {temp}, Humidity: {humidity}")
        except Exception as e:
            print("Error:", e)
