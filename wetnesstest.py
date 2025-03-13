import time
from wetness import read_moisture

while True:
    moisture = read_moisture()
    print(f"Soil Moisture: {moisture}%")
    time.sleep(1)